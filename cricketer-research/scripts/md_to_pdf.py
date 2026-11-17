#!/usr/bin/env python3
"""Render a cricketer-research dossier (Markdown) as a formatted PDF.

Usage:
    md_to_pdf.py INPUT.md [OUTPUT.pdf] [--page-size letter|a4]

OUTPUT defaults to INPUT with a .pdf extension.

Handles the Markdown the dossiers use: headings, paragraphs, nested bullet and
numbered lists, tables, bold and italic, inline code, links and bare URLs,
block quotes, horizontal rules and fenced code.

Any table that scores dimensions out of 10 (cells such as "8/10") also gets a
horizontal bar chart drawn under it. A table with two or more score columns,
as in a comparison, becomes a grouped chart with a legend.

Cricket's not-out asterisk ("254*", "100*") is left alone by the italic rules.

Requires reportlab. scripts/make_pdf.sh finds or installs it.
"""
import argparse
import os
import re
import sys

from reportlab.graphics.shapes import Drawing, Line, Rect, String
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.platypus import (
    BaseDocTemplate,
    CondPageBreak,
    Frame,
    HRFlowable,
    KeepTogether,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
    Table,
    TableStyle,
)

# ---------------------------------------------------------------- palette
# Text and chart colours follow the dataviz reference palette (light mode).
TEXT = colors.HexColor("#0b0b0b")
TEXT2 = colors.HexColor("#52514e")
GRID = colors.HexColor("#d9d8d4")
RULE = colors.HexColor("#c3c2b7")
HEAD_BG = colors.HexColor("#f0efec")
ZEBRA = colors.HexColor("#fafaf8")
TITLE = colors.HexColor("#104281")
H2 = colors.HexColor("#184f95")
LINK = "#256abf"
SERIES = [colors.HexColor(h) for h in ("#2a78d6", "#eb6834", "#1baf7a", "#eda100")]

# ---------------------------------------------------------------- fonts
FONT_SETS = [
    ("/System/Library/Fonts/Supplemental/", "Arial.ttf", "Arial Bold.ttf", "Arial Italic.ttf", "Arial Bold Italic.ttf"),
    ("/Library/Fonts/", "Arial.ttf", "Arial Bold.ttf", "Arial Italic.ttf", "Arial Bold Italic.ttf"),
    ("/usr/share/fonts/truetype/dejavu/", "DejaVuSans.ttf", "DejaVuSans-Bold.ttf", "DejaVuSans-Oblique.ttf", "DejaVuSans-BoldOblique.ttf"),
    ("/usr/share/fonts/dejavu/", "DejaVuSans.ttf", "DejaVuSans-Bold.ttf", "DejaVuSans-Oblique.ttf", "DejaVuSans-BoldOblique.ttf"),
    ("C:/Windows/Fonts/", "arial.ttf", "arialbd.ttf", "ariali.ttf", "arialbi.ttf"),
]
FALLBACK_FONTS = [
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    "/Library/Fonts/Arial Unicode.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
]
# Used only when neither the body font nor the fallback has the glyph.
ASCII_MAP = {
    "\u20b9": "Rs ", "\u2192": "->", "\u2190": "<-", "\u2248": "~", "\u2265": ">=",
    "\u2264": "<=", "\u2713": "yes", "\u2717": "no", "\u2605": "*", "\u2020": "+",
    "\u2014": "-", "\u2013": "-", "\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"',
    "\u00b7": "-", "\u2026": "...",
}

BODY, BOLD, MONO = "Helvetica", "Helvetica-Bold", "Courier"
FALLBACK = None
MAIN_CHARS = None      # None means "check by encoding" (built-in fonts)
FALLBACK_CHARS = set()
REPLACED = set()       # characters no font could draw
COMPLEX = set()        # characters drawn but needing shaping reportlab lacks
# Arabic-script and Hebrew need joining and right-to-left order; Indic and
# Southeast Asian scripts need conjunct shaping. reportlab does neither.
COMPLEX_RANGES = [(0x0590, 0x08FF), (0xFB1D, 0xFDFF), (0xFE70, 0xFEFF), (0x0900, 0x0DFF), (0x0E00, 0x0EFF), (0x1000, 0x109F)]


def _cmap(font):
    face = getattr(font, "face", None)
    return set(getattr(face, "charToGlyph", {}) or {})


def setup_fonts():
    global BODY, BOLD, MAIN_CHARS, FALLBACK, FALLBACK_CHARS
    for base, reg, bold, ital, boldital in FONT_SETS:
        paths = [os.path.join(base, f) for f in (reg, bold, ital, boldital)]
        if not all(os.path.exists(p) for p in paths):
            continue
        try:
            fonts = [TTFont(n, p) for n, p in zip(("Body", "Body-Bold", "Body-Italic", "Body-BoldItalic"), paths)]
        except Exception:
            continue
        for f in fonts:
            pdfmetrics.registerFont(f)
        pdfmetrics.registerFontFamily("Body", normal="Body", bold="Body-Bold", italic="Body-Italic", boldItalic="Body-BoldItalic")
        BODY, BOLD = "Body", "Body-Bold"
        MAIN_CHARS = _cmap(fonts[0]) or None
        break
    for p in FALLBACK_FONTS:
        if os.path.exists(p):
            try:
                f = TTFont("Fallback", p)
            except Exception:
                continue
            pdfmetrics.registerFont(f)
            FALLBACK, FALLBACK_CHARS = "Fallback", _cmap(f)
            break


def _supported(ch):
    if MAIN_CHARS is None:  # built-in Helvetica: WinAnsi only
        try:
            ch.encode("cp1252")
            return True
        except UnicodeEncodeError:
            return False
    return ord(ch) in MAIN_CHARS


def esc(s):
    """XML-escape text and route characters the body font lacks."""
    out = []
    for ch in s:
        if any(a <= ord(ch) <= b for a, b in COMPLEX_RANGES):
            COMPLEX.add(ch)
        if ch == "&":
            out.append("&amp;")
        elif ch == "<":
            out.append("&lt;")
        elif ch == ">":
            out.append("&gt;")
        elif ord(ch) < 128 or _supported(ch):
            out.append(ch)
        elif FALLBACK and ord(ch) in FALLBACK_CHARS:
            out.append('<font name="%s">%s</font>' % (FALLBACK, ch))
        else:
            if ch not in ASCII_MAP:
                REPLACED.add(ch)
            out.append(ASCII_MAP.get(ch, "?"))
    return "".join(out)


# ---------------------------------------------------------------- inline markdown
URL = r"https?://(?:[^\s()<>\[\]]|\([^\s()<>]*\))+"


def link(url, label):
    href = url.replace("&", "&amp;").replace('"', "&quot;")
    return '<a href="%s" color="%s">%s</a>' % (href, LINK, label)


def inline(text):
    """Convert one line of inline Markdown to reportlab paragraph markup."""
    stash = []

    def keep(markup):
        stash.append(markup)
        return "\x01%d\x02" % (len(stash) - 1)

    text = re.sub(r"<br\s*/?>", lambda m: keep("<br/>"), text)
    text = re.sub(r"\\([\\`*_\[\]()#|>-])", lambda m: keep(esc(m.group(1))), text)
    text = re.sub(r"`([^`]+)`", lambda m: keep('<font name="%s">%s</font>' % (MONO, esc(m.group(1)))), text)
    text = re.sub(r"\[([^\]]+)\]\((" + URL + r")\)", lambda m: keep(link(m.group(2), inline(m.group(1)))), text)

    def bare(m):
        url, trail = m.group(0), ""
        while url and url[-1] in ".,;:!?":
            trail, url = url[-1] + trail, url[:-1]
        return keep(link(url, esc(url))) + trail

    text = re.sub(URL, bare, text)
    text = esc(text)
    # Bold. "**254***" is bold "254*" (a not-out score), hence the trailing \** and (?!\*).
    text = re.sub(r"\*\*(?=\S)(.+?\**)(?<=\S)\*\*(?!\*)", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\w)__(?=\S)(.+?)(?<=\S)__(?!\w)", r"<b>\1</b>", text)
    # Italic. An opening * may not follow a letter or digit, so "254* and 100*" stays literal.
    text = re.sub(r"(?<![\w*])\*(?=[^\s*\d])(.+?)(?<=[^\s*])\*(?![\w*])", r"<i>\1</i>", text)
    text = re.sub(r"(?<!\w)_(?=\S)(.+?)(?<=\S)_(?!\w)", r"<i>\1</i>", text)
    while "\x01" in text:
        text = re.sub(r"\x01(\d+)\x02", lambda m: stash[int(m.group(1))], text)
    return text


def plain(text):
    """Text with Markdown markup removed, for measuring and labels."""
    text = re.sub(r"\[([^\]]+)\]\(" + URL + r"\)", r"\1", text)
    text = re.sub(r"<br\s*/?>", " ", text)
    text = re.sub(r"\*\*(.+?\**)\*\*(?!\*)", r"\1", text)
    text = re.sub(r"(?<![\w*])\*(?=[^\s*\d])(.+?)(?<=[^\s*])\*(?![\w*])", r"\1", text)
    text = text.replace("`", "")
    return re.sub(r"\\(.)", r"\1", text).strip()


# ---------------------------------------------------------------- styles
def make_styles():
    base = dict(fontName=BODY, textColor=TEXT, splitLongWords=1)
    s = {}
    s["title"] = ParagraphStyle("title", fontName=BOLD, fontSize=20, leading=24, textColor=TITLE, spaceAfter=4)
    s["h1"] = ParagraphStyle("h1", fontName=BOLD, fontSize=16, leading=20, textColor=TITLE, spaceBefore=14, spaceAfter=6, keepWithNext=1)
    s["h2"] = ParagraphStyle("h2", fontName=BOLD, fontSize=13.5, leading=17, textColor=H2, spaceBefore=14, spaceAfter=2, keepWithNext=1)
    s["h3"] = ParagraphStyle("h3", fontName=BOLD, fontSize=11, leading=14, textColor=TEXT, spaceBefore=10, spaceAfter=3, keepWithNext=1)
    s["h4"] = ParagraphStyle("h4", fontName=BOLD, fontSize=10, leading=13, textColor=TEXT2, spaceBefore=8, spaceAfter=2, keepWithNext=1)
    s["body"] = ParagraphStyle("body", fontSize=9.5, leading=13.5, spaceAfter=6, **base)
    s["quote"] = ParagraphStyle("quote", parent=s["body"], leftIndent=14, textColor=TEXT2, fontName=BODY)
    s["code"] = ParagraphStyle("code", fontName=MONO, fontSize=8, leading=10, textColor=TEXT, leftIndent=8, spaceAfter=6)
    s["caption"] = ParagraphStyle("caption", fontName=BOLD, fontSize=9, leading=12, textColor=TEXT2, spaceBefore=6, spaceAfter=2)
    return s


def para(markup, style, fallback_text=None):
    """Paragraph that degrades to plain escaped text if the markup will not parse."""
    try:
        return Paragraph(markup, style)
    except Exception:
        return Paragraph(esc(plain(fallback_text if fallback_text is not None else markup)), style)


# ---------------------------------------------------------------- block parsing
LIST_RE = re.compile(r"^(\s*)([-*+\u2022]|\d+[.)])\s+(.*)$")
SEP_RE = re.compile(r"^\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")
HEAD_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
HR_RE = re.compile(r"^(-{3,}|\*{3,}|_{3,})$")


def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|") and not line.endswith("\\|"):
        line = line[:-1]
    return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", line)]


def parse_aligns(sep):
    out = []
    for c in split_row(sep):
        c = c.strip()
        out.append("CENTER" if c.startswith(":") and c.endswith(":") else "RIGHT" if c.endswith(":") else "LEFT")
    return out


def starts_block(line):
    s = line.strip()
    return bool(HEAD_RE.match(s) or HR_RE.match(s) or s.startswith("|") or s.startswith("```") or s.startswith(">") or LIST_RE.match(line))


def parse_blocks(md):
    lines = md.replace("\r\n", "\n").replace("\t", "    ").split("\n")
    blocks, i = [], 0
    while i < len(lines):
        line, s = lines[i], lines[i].strip()
        if not s:
            i += 1
            continue
        if s.startswith("```"):
            j, buf = i + 1, []
            while j < len(lines) and not lines[j].strip().startswith("```"):
                buf.append(lines[j])
                j += 1
            blocks.append(("code", "\n".join(buf)))
            i = j + 1
            continue
        m = HEAD_RE.match(s)
        if m:
            blocks.append(("h", len(m.group(1)), m.group(2)))
            i += 1
            continue
        if HR_RE.match(s):
            blocks.append(("hr",))
            i += 1
            continue
        if s.startswith("|") and i + 1 < len(lines) and SEP_RE.match(lines[i + 1].strip()):
            rows, aligns, j = [split_row(s)], parse_aligns(lines[i + 1]), i + 2
            while j < len(lines) and lines[j].strip().startswith("|"):
                rows.append(split_row(lines[j]))
                j += 1
            blocks.append(("table", rows, aligns))
            i = j
            continue
        if s.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip()[1:].strip())
                i += 1
            blocks.append(("quote", " ".join(buf)))
            continue
        if LIST_RE.match(line):
            items, after_blank = [], False   # item: [indent, marker or None, text]
            while i < len(lines):
                cur = lines[i]
                m = LIST_RE.match(cur)
                if m:
                    items.append([len(m.group(1)), m.group(2), m.group(3)])
                    after_blank = False
                    i += 1
                    continue
                if not cur.strip():
                    k = i + 1
                    while k < len(lines) and not lines[k].strip():
                        k += 1
                    if k < len(lines) and (LIST_RE.match(lines[k]) or (lines[k].startswith("  ") and not lines[k].strip().startswith("|"))):
                        i, after_blank = k, True
                        continue
                    break
                if cur.startswith("  ") and not starts_block(cur):
                    if after_blank:  # an indented paragraph inside the list
                        items.append([len(cur) - len(cur.lstrip()), None, cur.strip()])
                    else:            # a wrapped line of the previous item
                        items[-1][2] += " " + cur.strip()
                    after_blank = False
                    i += 1
                    continue
                if not after_blank and not starts_block(cur):  # lazy continuation
                    items[-1][2] += " " + cur.strip()
                    i += 1
                    continue
                break
            blocks.append(("list", items))
            continue
        buf = [s]
        i += 1
        while i < len(lines) and lines[i].strip() and not starts_block(lines[i]):
            buf.append(lines[i].strip())
            i += 1
        blocks.append(("p", " ".join(buf)))
    return blocks


# ---------------------------------------------------------------- tables
NUMERIC_RE = re.compile(r"^[\d,.\s*/%+\-\u2013\u2014()]+$|^[-\u2013\u2014]$")


def make_table(rows, aligns, avail, styles):
    ncols = max(len(r) for r in rows)
    rows = [r + [""] * (ncols - len(r)) for r in rows]
    aligns = (aligns + ["LEFT"] * ncols)[:ncols]
    fs = 8.3 if ncols >= 7 else 8.8
    pad = 4
    body_rows = rows[1:]
    for c in range(ncols):  # right-align columns that hold only numbers
        cells = [plain(r[c]) for r in body_rows if plain(r[c])]
        if aligns[c] == "LEFT" and cells and c > 0 and all(NUMERIC_RE.match(x) for x in cells):
            aligns[c] = "RIGHT"
    amap = {"LEFT": TA_LEFT, "RIGHT": TA_RIGHT, "CENTER": TA_CENTER}
    head_st = [ParagraphStyle("th%d" % c, fontName=BOLD, fontSize=fs, leading=fs * 1.25, textColor=TEXT, alignment=amap[aligns[c]], splitLongWords=1) for c in range(ncols)]
    cell_st = [ParagraphStyle("td%d" % c, fontName=BODY, fontSize=fs, leading=fs * 1.3, textColor=TEXT, alignment=amap[aligns[c]], splitLongWords=1) for c in range(ncols)]

    nat, mins = [], []
    for c in range(ncols):
        n, mn = 0.0, 0.0
        for ri, r in enumerate(rows):
            t = plain(r[c])
            font = BOLD if ri == 0 or r[c].startswith("**") else BODY
            n = max(n, pdfmetrics.stringWidth(t, font, fs))
            for w in t.split():
                mn = max(mn, pdfmetrics.stringWidth(w, font, fs))
        nat.append(min(n, avail) + 2 * pad + 1)
        mins.append(min(mn, 1.4 * inch) + 2 * pad + 1)
    if sum(nat) <= avail:
        extra = avail - sum(nat)
        widths = [w + extra / ncols for w in nat]
    elif sum(mins) >= avail:
        widths = [avail * m / sum(mins) for m in mins]
    else:
        room = avail - sum(mins)
        flex = [max(n - m, 0.0) for n, m in zip(nat, mins)]
        tot = sum(flex) or 1.0
        widths = [m + room * f / tot for m, f in zip(mins, flex)]

    data = []
    for ri, r in enumerate(rows):
        st = head_st if ri == 0 else cell_st
        data.append([para(inline(cell), st[c], cell) for c, cell in enumerate(r)])
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), HEAD_BG),
        ("LINEBELOW", (0, 0), (-1, 0), 0.8, TEXT2),
        ("LINEBELOW", (0, 1), (-1, -1), 0.4, GRID),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, ZEBRA]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), pad),
        ("RIGHTPADDING", (0, 0), (-1, -1), pad),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
    ]))
    return t


# ---------------------------------------------------------------- ratings chart
SCORE_RE = re.compile(r"^\W*(\d+(?:\.\d+)?)\s*/\s*10(?!\d)")
BARE_NUM_RE = re.compile(r"^\W*(\d+(?:\.\d+)?)\W*$")


def ratings_from_table(rows):
    header, body = rows[0], rows[1:]
    body = [r for r in body if r and not re.match(r"^\W*(total|overall)\b", plain(r[0]), re.I)]
    if len(body) < 3:
        return None
    cols = []
    for c in range(1, len(header)):
        vals = []
        for r in body:
            t = plain(r[c]) if c < len(r) else ""
            m = SCORE_RE.match(t)
            if not m and re.search(r"score|rating|/\s*10", plain(header[c]), re.I):
                m = BARE_NUM_RE.match(t)
            if not m or float(m.group(1)) > 10:
                vals = None
                break
            vals.append(float(m.group(1)))
        if vals:
            cols.append((plain(header[c]), vals))
    if not cols:
        return None
    return [plain(r[0]) for r in body], cols


def _fit(text, font, size, width):
    if pdfmetrics.stringWidth(text, font, size) <= width:
        return text
    while text and pdfmetrics.stringWidth(text + "\u2026", font, size) > width:
        text = text[:-1]
    return text.rstrip() + "\u2026"


def _bar(d, x, y, w, h, color):
    """Bar with a rounded data end and a square baseline end."""
    if w <= 0:
        return
    r = min(2.5, w / 2, h / 2)
    d.add(Rect(x, y, w, h, rx=r, ry=r, fillColor=color, strokeColor=None))
    d.add(Rect(x, y, min(w, r + 0.5), h, fillColor=color, strokeColor=None))


def _wrap2(text, font, size, width):
    """Split a label into at most two lines that fit width; trim the second if needed."""
    if pdfmetrics.stringWidth(text, font, size) <= width:
        return [text]
    words, first = text.split(), ""
    for k in range(len(words), 0, -1):
        cand = " ".join(words[:k])
        if pdfmetrics.stringWidth(cand, font, size) <= width:
            first = cand
            rest = " ".join(words[k:])
            return [first, _fit(rest, font, size, width)] if rest else [first]
    return [_fit(text, font, size, width)]


def ratings_chart(labels, series, width):
    n = len(series)
    bar_h = 9.0 if n == 1 else 7.0
    gap = 2.0
    group_h = n * bar_h + (n - 1) * gap
    lab_size, lab_lead = 8.5, 9.5
    label_w = min(max(pdfmetrics.stringWidth(l, BODY, lab_size) for l in labels) + 10, width * 0.34)
    wrapped = [_wrap2(l, BODY, lab_size, label_w - 10) for l in labels]
    two_line = any(len(w) > 1 for w in wrapped)
    group_gap = 7.0 if n == 1 else 9.0
    pitch = max(group_h + group_gap, (2 * lab_lead + 4) if two_line else 0)
    value_w = 26.0
    plot_x, plot_w = label_w, width - label_w - value_w
    legend_h = 16.0 if n > 1 else 0.0
    axis_h = 14.0
    h = legend_h + len(labels) * pitch + axis_h + 2
    d = Drawing(width, h)
    y_top, y_bot = h - legend_h - 2, axis_h
    for v in range(0, 11, 2):
        x = plot_x + plot_w * v / 10.0
        d.add(Line(x, y_bot, x, y_top, strokeColor=GRID, strokeWidth=0.5 if v else 0.9))
        d.add(String(x, y_bot - 10, str(v), fontName=BODY, fontSize=7, fillColor=TEXT2, textAnchor="middle"))
    if n > 1:
        lx = plot_x
        for si, (name, _) in enumerate(series):
            d.add(Rect(lx, h - 11, 8, 8, rx=1.5, ry=1.5, fillColor=SERIES[si % len(SERIES)], strokeColor=None))
            d.add(String(lx + 11, h - 10, name, fontName=BODY, fontSize=8, fillColor=TEXT))
            lx += 11 + pdfmetrics.stringWidth(name, BODY, 8) + 16
    for gi, lines in enumerate(wrapped):
        row_top = y_top - gi * pitch
        cy = row_top - pitch / 2
        g_top = cy + group_h / 2
        first_base = cy - 3 + (lab_lead / 2 if len(lines) == 2 else 0)
        for li, line in enumerate(lines):
            d.add(String(plot_x - 6, first_base - li * lab_lead, line, fontName=BODY, fontSize=lab_size, fillColor=TEXT, textAnchor="end"))
        for si, (_, vals) in enumerate(series):
            v = max(0.0, min(vals[gi], 10.0))
            by = g_top - (si + 1) * bar_h - si * gap
            bw = plot_w * v / 10.0
            _bar(d, plot_x, by, bw, bar_h, SERIES[si % len(SERIES)])
            d.add(String(plot_x + bw + 3, by + bar_h / 2 - 2.6, "%g" % vals[gi], fontName=BODY, fontSize=7.5, fillColor=TEXT))
    return d


# ---------------------------------------------------------------- document
class NumberedCanvas(rl_canvas.Canvas):
    doc_title = ""
    page_count = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._pages = []

    def showPage(self):
        self._pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total = len(self._pages)
        NumberedCanvas.page_count = total
        for state in self._pages:
            self.__dict__.update(state)
            self._footer(total)
            super().showPage()
        super().save()

    def _footer(self, total):
        w, _ = self._pagesize
        m = 0.75 * inch
        self.setStrokeColor(GRID)
        self.setLineWidth(0.5)
        self.line(m, 0.6 * inch, w - m, 0.6 * inch)
        self.setFont(BODY, 7.5)
        self.setFillColor(TEXT2)
        title = "".join(c if (ord(c) < 128 or _supported(c)) else ASCII_MAP.get(c, "?") for c in self.doc_title)
        self.drawString(m, 0.45 * inch, _fit(title, BODY, 7.5, w - 2 * m - 70))
        self.drawRightString(w - m, 0.45 * inch, "Page %d of %d" % (self._pageNumber, total))


def build(md_path, pdf_path, pagesize):
    setup_fonts()
    styles = make_styles()
    md = open(md_path, encoding="utf-8").read()
    blocks = parse_blocks(md)

    title = next((b[2] for b in blocks if b[0] == "h" and b[1] == 1), None)
    if title is None:
        title = os.path.splitext(os.path.basename(md_path))[0].replace("-", " ").title()
    NumberedCanvas.doc_title = plain(title)

    margin = 0.75 * inch
    doc = BaseDocTemplate(
        pdf_path, pagesize=pagesize, leftMargin=margin, rightMargin=margin,
        topMargin=0.7 * inch, bottomMargin=0.85 * inch,
        title=plain(title), author="cricketer-research", subject="Cricketer research dossier",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="body", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="page", frames=[frame])])
    avail = doc.width

    story, title_done = [], False
    for b in blocks:
        kind = b[0]
        if kind == "h":
            level, text = b[1], b[2]
            if level == 1 and not title_done:
                story.append(para(inline(text), styles["title"], text))
                story.append(HRFlowable(width="100%", thickness=1.2, color=H2, spaceBefore=2, spaceAfter=10))
                title_done = True
                continue
            if level <= 2:
                story.append(CondPageBreak(1.1 * inch))
            st = styles["h1"] if level == 1 else styles["h2"] if level == 2 else styles["h3"] if level == 3 else styles["h4"]
            story.append(para(inline(text), st, text))
            if level == 2:
                story.append(HRFlowable(width="100%", thickness=0.5, color=RULE, spaceBefore=1, spaceAfter=6))
        elif kind == "p":
            story.append(para(inline(b[1]), styles["body"], b[1]))
        elif kind == "quote":
            story.append(para(inline(b[1]), styles["quote"], b[1]))
        elif kind == "code":
            story.append(Preformatted(b[1], styles["code"]))
        elif kind == "hr":
            story.append(HRFlowable(width="100%", thickness=0.5, color=RULE, spaceBefore=4, spaceAfter=8))
        elif kind == "list":
            items = b[1]
            indents = sorted({it[0] for it in items if it[1] is not None}) or [0]

            def level_of(ind):
                lv = 0
                for k, v in enumerate(indents):
                    if ind >= v:
                        lv = k
                return lv

            last_level = 0
            for k, (ind, marker, text) in enumerate(items):
                if marker is None:
                    lv = min(level_of(ind), last_level)
                    st = ParagraphStyle("lc", parent=styles["body"], leftIndent=16 * (lv + 1), spaceAfter=3)
                    story.append(para(inline(text), st, text))
                    continue
                lv = level_of(ind)
                last_level = lv
                ordered = marker[0].isdigit()
                bullet = marker if ordered else ("\u2022" if lv % 2 == 0 else "\u2013")
                nxt_is_child = k + 1 < len(items) and items[k + 1][1] is not None and level_of(items[k + 1][0]) > lv
                st = ParagraphStyle(
                    "li", parent=styles["body"], leftIndent=16 * (lv + 1), bulletIndent=16 * lv + 3,
                    bulletFontName=BODY, spaceAfter=1.5 if nxt_is_child else 3,
                )
                story.append(_li(inline(text), st, bullet, text))
            story.append(Spacer(1, 3))
        elif kind == "table":
            rows, aligns = b[1], b[2]
            story.append(make_table(rows, aligns, avail, styles))
            story.append(Spacer(1, 8))
            found = ratings_from_table(rows)
            if found:
                labels, series = found
                cap = "Attribute ratings, out of 10" if len(series) == 1 else "Attribute ratings, out of 10: " + " v ".join(s[0] for s in series)
                story.append(KeepTogether([
                    para(esc(cap), styles["caption"]),
                    ratings_chart(labels, series, min(avail, 6.0 * inch)),
                    Spacer(1, 10),
                ]))
    doc.build(story, canvasmaker=NumberedCanvas)
    return NumberedCanvas.page_count


def _li(markup, style, bullet, raw):
    try:
        return Paragraph(markup, style, bulletText=bullet)
    except Exception:
        return Paragraph(esc(plain(raw)), style, bulletText=bullet)


def main():
    ap = argparse.ArgumentParser(description="Render a cricketer-research Markdown dossier as a PDF.")
    ap.add_argument("input")
    ap.add_argument("output", nargs="?")
    ap.add_argument("--page-size", choices=["letter", "a4"], default="letter")
    a = ap.parse_args()
    out = a.output or os.path.splitext(a.input)[0] + ".pdf"
    pages = build(a.input, out, letter if a.page_size == "letter" else A4)
    print("Wrote %s (%d pages)" % (out, pages))
    if REPLACED:
        print("Warning: no font has these characters; each printed as '?': %s" % " ".join(sorted(REPLACED)), file=sys.stderr)
    if COMPLEX:
        print("Warning: non-Latin script found (%d characters, e.g. %s). The PDF cannot join or reorder it, so it prints garbled. "
              "Use the Latin-script form in the Markdown and rebuild." % (len(COMPLEX), "".join(sorted(COMPLEX))[:12]), file=sys.stderr)


if __name__ == "__main__":
    sys.exit(main())
