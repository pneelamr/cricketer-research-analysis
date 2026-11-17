---
name: cricketer-research
description: Produce a structured, source-verified research dossier, delivered as a formatted PDF, on any cricketer — men's or women's, from any country or era, international, domestic or franchise — or a head-to-head comparison of two or more players. Use this whenever the user names a cricketer and wants them researched, profiled, analyzed, scouted, rated, or compared: phrasings like "research [player]", "profile on [player]", "[player] career and stats", "how good is [player]", "tell me about [player]", "compare [A] and [B]", "who's the better Test batter, X or Y", "make me a PDF on [player]", or just pasting a cricketer's name and expecting a write-up. Trigger even when the user never says the word "cricket" but the name is clearly a cricketer, and for lesser-known associate-nation, domestic-only, women's, or historic players. Do not use for live scores, fixtures, fantasy-team selection, or questions about teams and tournaments rather than individual players.
---

# Cricketer Research

This skill turns a cricketer's name into a consistent, well-sourced research dossier: a verified identity header, career statistics by format, a career arc, a technical and tactical profile, a parameters table, role-appropriate attribute ratings out of 10, records, and a source list. Two or more names with "compare", "vs", or "who is better" switch it into comparison mode.

The goal is a dossier the reader can trust on the numbers and find genuinely illuminating on the judgement calls. Three failure modes to guard against, each handled explicitly below:

1. **Wrong or stale numbers.** Model memory for cricket statistics is unreliable, and an active player's figures change every week. Every number must come from a search done now, stamped with its date.
2. **The wrong player.** Cricket is full of shared names (two Steve Smiths, two Mohammad Hafeezs, three Rahuls, a men's and a women's Smriti). Pin the identity down before researching.
3. **Format confusion.** T20 (all matches) is not T20I. First-class is not Test. List A is not ODI. Mixing these produces numbers that look plausible and are wrong.

## Input

The user supplies one or more player names, optionally with a team, era, or format in mind. Treat "research", "profile", "tell me about", "how good is", "scout", and "rate" as requests for the single-player dossier. Treat two or more names joined by "compare", "vs", "versus", "or", or "who is better" as a comparison request (see the comparison section).

If the user names a specific angle ("as a Test batter", "in the IPL", "against spin"), keep the full dossier structure but weight the analysis and the ratings toward that angle and say so.

If the user says what the research is for (an article on a theme, a scouting report, a debate, a quiz), add an **angle section** that serves that purpose directly; see "Angle section" under Step 2. The standard sections make dossiers comparable, but the angle section is where the user's actual question gets answered, so it deserves the most digging.

## Step 0 — Pin down who you are researching

Before any statistics, confirm the player's identity: full name, country, gender, role, and whether they are active or retired. Search the name and check which cricketer the user most plausibly means:

- A bare surname or common name gets the most prominent current or historical match, with a one-line note of the alternative you ruled out ("Taking this as Steven Smith of Australia, not Graeme Smith of South Africa").
- A name shared across men's and women's cricket: use context (teams, formats, tournaments mentioned) and default to the more prominent player. Name the other one in a line so the user can redirect.
- Do not assume a cricketer is a man. Women's internationals, the WPL, WBBL, The Hundred, and the Women's Premier League are squarely in scope.
- Spelling varies across sources (transliteration of South Asian, Afghan, and Sri Lankan names). Use the spelling ESPNcricinfo uses, and mention common variants once.

If the name is genuinely ambiguous and context gives no steer, pick the most prominent player, say which one you picked and why, and proceed. Do not stall on a question when a stated assumption will do.

## Step 1 — Verify, don't recall

Use the web search tool for every factual claim that matters: biographical facts, debut dates, career figures, records, captaincy spells, awards. Read `references/sources.md` before the first search. It says which sites hold which facts and, just as important, which ones refuse automated fetching. ESPNcricinfo profiles, Statsguru, HowSTAT and Cricbuzz blocked every fetch in testing, so the working route is usually the Wikipedia infobox (which cites ESPNcricinfo with a date) cross-checked against the cricket.com.au player page, with the blocked sites read through search-result snippets.

Research efficiently. Send independent searches together in one round. Try a blocked site once, then move to the fallback; do not retry it or work around the block with shell tools. A good dossier usually needs fifteen to twenty-five well-chosen lookups, and once every section has its facts from a reliable source, stop searching and write.

Minimum verification before writing:

- Identity and biography from a profile page (ESPNcricinfo profile, or Wikipedia as a second source).
- Career figures for each international format from a statistics page, cross-checked against a second source for the headline numbers (matches, runs, average, wickets). Two sources disagreeing by a match or two usually means one was captured before the latest game; take the newer and say so.
- Records and "firsts" from the record-keeping source itself, not from a news article's paraphrase.
- For active players, the most recent series or tournament, so the dossier reflects current form and current team status.

When reputable sources disagree on any fact, statistical or biographical (a debut year, a citizenship date, a reason for a move, a record count), give both values with their sources instead of silently picking one. A reader writing about the player needs to know which facts are contested.

Prefer the most recent dated figure for splits (home and away, by opponent, as captain) and records. Search with the current year in the query, because an older article's split can be a year or more out of date.

Write the retrieval date on the statistics ("Stats as of 15 Nov 2026, ESPNcricinfo"). For retired players, say "final career figures" instead. If a figure cannot be confirmed from a reliable source, say "unconfirmed" next to it rather than writing a number from memory. A visibly missing number costs far less credibility than a confidently wrong one.

## Step 2 — The dossier

Present the sections below in this order. Use the headings as written so dossiers stay comparable across players.

### Identity header

A compact block, each line verified:

- **Full name** (and the name they are known by, if different)
- **Born** — date and place; **Died** if applicable
- **Country / teams** — national side, plus the domestic and franchise sides that matter to their career
- **Role** — e.g. right-hand top-order batter; left-arm orthodox spinner; wicketkeeper-batter; batting all-rounder
- **Batting / bowling style** — hand and type, as the record books list them
- **International debuts** — one line per format with year and opponent
- **Status** — active (current teams and formats) or retired (year and last match), and any captaincy
- **Stats as of** — the date and source for the tables that follow

### Career statistics

Two tables, batting and bowling. Drop the one that does not apply to a specialist (a pure batter who has bowled a handful of overs gets a single line noting that instead of a table). Include one row per international format the player has played; add First-class, List A, or T20 (all matches) rows when the player is primarily a domestic cricketer or when the franchise career is a major part of the story.

| Format | Mat | Inns | Runs | HS | Avg | SR | 100 | 50 |
|---|---|---|---|---|---|---|---|---|
| Tests | | | | | | | | |
| ODIs | | | | | | | | |
| T20Is | | | | | | | | |

| Format | Mat | Balls | Wkts | BBI | Avg | Econ | SR | 5w |
|---|---|---|---|---|---|---|---|---|

Add catches and stumpings as a line under the tables for wicketkeepers and standout fielders. Keep these as actual numbers; do not pad with "approx." If a cell is genuinely unavailable (common for older women's and associate-nation cricket), leave a dash and say why in a note below the table.

### Career arc

Bullet points, chronological, covering debut and breakthrough, peak years, dips (injury, form, selection), captaincy and leadership roles, defining series or tournaments, retirement or current standing. The point is to explain the shape of the career, not to list every season. Six to twelve bullets is the usual range; a long career earns more, a short one fewer.

### Angle section (when the user states a purpose)

Title it for the purpose, for example "Playing for an adopted country" or "Scouting notes for the IPL auction". Gather the documented material that serves it:

- the player's own words on the subject, as short direct quotes with source and date
- the matches or moments that best illustrate it, with figures
- how the relevant audiences (fans, boards, media in each country involved) have received it
- the contested or unclear points, presented as contested, with each side's source
- comparable players when the purpose calls for them

Skip this section when the user gives no purpose; do not invent one.

### Playing style and technical profile

Bullet points on how they actually play: batting setup and signature shots, strengths and vulnerabilities against pace and spin, bowling action, pace or flight, variations and plans, fielding position and quality, temperament and match situations they are known for. Draw on documented analysis (coach and commentator assessments, ESPNcricinfo profile text, recognised cricket writers), not just the statistics. Where the numbers illustrate a stylistic point (a huge gap between home and away average, a strike rate that jumped after a technique change), bring them in.

### Overall parameters

A two-column summary table:

| Parameter | Description |
|---|---|
| Role | … |
| Era and teams | … |
| Defining strength | … |
| Main vulnerability | … |
| Standing / legacy | … |
| Closest comparisons | … |

Add a row when it earns its place (e.g. **Format where they are strongest**, **Signature performance**). Keep each cell to a tight phrase or sentence; the table is a scannable summary.

### Attribute ratings (out of 10)

Pick six to eight dimensions that fit the player's role, score each out of 10, and justify each score in one line with evidence (a number, a series, a documented trait). The scale is anchored so ratings mean the same thing across dossiers:

- **10** — among the best ever in that dimension
- **8–9** — elite of their era
- **6–7** — good international standard
- **4–5** — average international standard, or strong domestic level
- **1–3** — a clear weakness

Suggested dimension sets, adjusted to the player:

- *Batter:* Technique and shot range · Consistency · Versatility across formats and conditions · Big-match impact · Longevity and durability · Fielding · Leadership or influence
- *Bowler:* Wicket-taking threat · Control and economy · Variation and skill range · Versatility across formats and conditions · Durability and workload · Big-match impact · Batting and fielding contribution
- *All-rounder:* Batting · Bowling · Match impact and balance · Versatility · Fielding · Durability · Leadership
- *Wicketkeeper:* Glovework · Keeping to spin · Keeping to pace · Batting · Fitness and durability · Leadership and tactical input

Present as a table:

| Dimension | Score | Why |
|---|---|---|
| … | …/10 | … |

Be honest with the scale. A dossier where every dimension is 9 says nothing; the value is in where the player is merely good, and why. Write every score as `n/10`. The PDF script recognises the table by that pattern and draws it as a horizontal bar chart beneath, so a score written any other way will not be charted.

### Records and milestones

Bullets: records held (current or former, say which), landmark performances, major awards (ICC awards, Wisden Cricketer of the Year, national honours), notable firsts. Each one verified, with the figure and the year.

### Recent form and current context

For active players only: performances over roughly the last twelve months, current ICC rankings if ranked, injuries, current contracts and franchise deals, and any selection or role changes. For retired players, replace this with a short **After playing** section (coaching, commentary, administration) when there is something documented to say.

### Off-field and context

Brief and factual. Captaincy record, documented disputes or sanctions, major injuries, philanthropy, or anything that materially shaped the career. Report only what reliable sources document, in neutral language, with the source; do not speculate about character, and skip the section if there is nothing substantive.

### Sources

Numbered list of the sources actually used, with URL and the date accessed. The reader should be able to re-check any number in the dossier from this list.

## Comparison mode

When the request names two or more players to compare, read `references/comparison-format.md` and follow that structure instead: shared identity header, side-by-side statistics per format, the same attribute dimensions scored for each player, a section on the context that makes raw comparison misleading (era, home versus away, bowling attacks faced, team strength, role), and a verdict that answers the user's actual question with reasoning and the conditions under which it would flip.

## Accuracy guardrails

These are the errors that recur in cricket research; check the dossier against them before delivering.

- **T20 versus T20I, first-class versus Test, List A versus ODI.** Label every table row with the exact category the source used.
- **Averages and strike rates are format-specific.** Never blend formats into a single "career average".
- **Stats drift.** Figures captured from a news article may be months old; a profile page updated after the last match is the reference. Stamp the date.
- **Debut dates.** Confirm the opponent and year; model memory frequently shifts these by a year.
- **Records expire.** A "fastest to 100 ODI wickets" record may have been broken; check whether it still stands and phrase it as "held the record from X until Y" if not.
- **Captaincy figures** (matches, wins) come from a stats query, not from memory.
- **Names and spellings** follow ESPNcricinfo. Mention variants once in the header.
- **Totals equal their parts.** Recompute every total you state from its components before delivering: catches across formats, international runs and hundreds across formats, rating totals in a comparison. A total that disagrees with its own parts by one is the kind of slip a reader spots first.
- **Contested facts stay contested.** If two reliable sources disagree, the dossier says so; it does not pick one and state it as settled.
- **Nothing invented.** If a fact cannot be verified, it is marked unconfirmed or omitted. Never fill a table cell to make it look complete.

## Delivering the output: a PDF

The deliverable is a formatted PDF, built from a Markdown source by a bundled script.

1. **Write the Markdown.** Save the dossier to `profiles/<firstname-lastname>.md`, or a comparison to `comparisons/<a>-vs-<b>.md`, in lowercase with hyphens, creating the folder if needed. Use plain Markdown in the section order above. The Markdown stays beside the PDF as the editable source, so a later correction or update only needs the PDF rebuilt.
2. **Build the PDF.** Run `scripts/make_pdf.sh` from this skill's directory on the Markdown file, for example `bash <skill-dir>/scripts/make_pdf.sh profiles/rashid-khan.md`. It writes `profiles/rashid-khan.pdf` next to the source and prints the page count. Add `--page-size a4` if the user wants A4; the default is US Letter. The script needs reportlab: it uses the system copy if there is one, and otherwise installs it once into a private environment under `~/.cache/cricketer-research`.
3. **Let the script do the layout.** It handles the title, headings, nested lists, wide statistics tables, clickable source links, page numbers, and a bar chart under any table of `n/10` scores (a grouped chart with a legend for comparisons). Do not hand-build a PDF or add layout code of your own; if something renders badly, fix the Markdown. Keep the text in Latin script and leave out emoji: the PDF cannot shape Urdu, Hindi or other non-Latin scripts, and it prints emoji as "?". The script warns when either happens; fix the Markdown and rebuild.
4. **Reply briefly in chat.** Give who the player is, three or four headline figures, the main judgement or the comparison verdict, anything that could not be verified, and the PDF's path. The full dossier is in the PDF, so do not paste it into the chat.

If the environment cannot run scripts or write files, give the full dossier in the chat as Markdown instead. If the user asks for a different destination or format, use that.

## Worked example (abbreviated)

**Input:** "Research Rashid Khan"

**Step 0:** Rashid Khan, Afghanistan leg-spinner (not the Pakistani domestic cricketer of the same name). Active.

**Identity header:** Rashid Khan Arman · born 20 September 1998, Nangarhar · Afghanistan; Gujarat Titans, Sunrisers Hyderabad, Adelaide Strikers, among others · right-arm leg-break, right-hand bat · debuts: ODI 2015 v Zimbabwe, T20I 2015 v Zimbabwe, Test 2018 v India · Stats as of [date], ESPNcricinfo.

**Career statistics:** bowling table with ODI, T20I, Test, and T20 (all) rows, since the franchise career is central; a short batting table because he is a genuine lower-order hitter.

**Career arc:** bullets from the 2015 debut, the 2017 IPL arrival, the 2019 fastest-to-100-ODI-wickets mark (44 matches, confirmed at the time of writing whether it still stands), captaincy spells, the 2023 back surgery, the 2024 T20 World Cup semi-final.

**Playing style:** bullets on the fast, flat leg-break and googly, the speed through the air that makes him hard to read, death-overs economy, and the batting cameos.

**Parameters table** and **attribute ratings** (bowler set), each score with a one-line reason, then records, recent form, off-field notes, and sources.

*(In a real run every figure above is confirmed by search before it is written.)*
