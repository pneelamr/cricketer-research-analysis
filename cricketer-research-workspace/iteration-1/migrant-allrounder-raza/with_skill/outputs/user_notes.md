# User notes — Sikandar Raza dossier (16 November 2026)

## How the research ran

The run was interrupted three times by usage-limit resets and finished under an instruction to stop issuing web requests and write up with the material in hand. Roughly 20 planned searches/fetches were never executed; the gaps they would have closed are listed below.

## Sources that failed to fetch

- **ESPNcricinfo player profile** — HTTP 403 (also reached via an espn.com redirect, which was not followed). Used only through search-result snippets. The skill names this as the primary statistics source, so the tables were sourced instead from Wikipedia's infobox (which credits Cricinfo, as of 12 November 2026) and cross-checked against cricket.com.au, which shows identical figures.
- **HowSTAT** (all-formats summary, Test, ODI, T20I pages) — HTTP 403 on every attempt, including a retry. Used only through search snippets (T20I best figures 5/18; Zimbabwe records).
- **Cricbuzz** — the domain blocks the search crawler entirely (API error), so no Cricbuzz data at all.
- **ESPNcricinfo SA20 story** ("Bereaved Raza makes a statement") — 403; content taken from the ESPN Africa mirror snippet and South African press instead.
- **Zimbabwe Independent** profile ("How a Pakistani boy became a cricket icon") — fetch returned the headline only.
- **ICC rankings pages** (T20I and ODI all-rounder) — fetch denied by the tool's permission classifier.
- **Wikipedia "List of Zimbabwe national cricket captains"** — fetch denied by the permission classifier; this was the planned source for captaincy win–loss figures.
- **Wisden PSL-final article** and **cricket.com captaincy article** — the first hit the usage limit, the second failed DNS. Both used at headline/snippet level only.
- A curl download was attempted once and denied by the permission system; not retried, per the coordinator's instruction.

## Figures and claims not confirmed

Statistics tables
- **List A and T20 (all matches) rows** — not obtained from any source. The dossier says so and warns against using the T20I row as a proxy.
- **First-class highest score** — infobox (Cricinfo-sourced) says 226; Wikipedia's body text says his best is 146. Left as "226 (unconfirmed)".
- **First-class innings and batting strike rate** — not shown by the sources; left as dashes.
- **T20I best bowling 5/18** — from the Cricinfo-sourced infobox (with one five-for); cricket.com.au shows 4/8 but also "5w: 1", which is internally inconsistent, so 5/18 was taken. The match (opponent, date) in which he took 5/18 was not confirmed.
- **Bowling strike rates** in both tables are derived (balls ÷ wickets) from the balls and wickets columns; the sources do not show SR directly.
- **Catches** — Test 7, ODI 64, T20I 66, FC 53 from the infobox; cricket.com.au agrees on the international figures.

Career and records
- **Year of the family's move to Zimbabwe** — Wikipedia says 2002; Al Jazeera and the Zimbabwe Independent say 2003. Both given in the dossier. No source explains why the family moved.
- **T20I captaincy appointment date** — "late 2023" is inferred from a cricket.com article URL timestamped early November 2023 and a Sportscast Zimbabwe headline; the article itself could not be fetched. Wikipedia gives "2023–present".
- **Captaincy win–loss record** (ODIs and T20Is) — not obtained. Leadership rating therefore rests on documented results rather than a W/L line.
- **2022 T20 World Cup win over Pakistan** (Perth) — the planned verification search was cut off. Raza's bowling in that match is widely cited but is explicitly flagged as unverified in the dossier.
- **ICC Men's T20I Team of the Year** — a Zimbabwe Independent headline says he was named; the year(s) were not confirmed.
- **ICC No. 1 ODI all-rounder, September 2025** — based on a Wisden headline ("39-year-old all-rounder crowned new No.1") whose URL points to Raza; the article body was not read.
- **Current ICC rankings (November 2026)** — last confirmed point is "still No. 1 T20I all-rounder" per Wisden on 1 July 2026. Nothing newer was found before requests were stopped.
- **"Still stands" status** of the Zimbabwe records cited (224 opening stand, fastest Zimbabwe ODI hundred, 135* from No. 5 or lower, second-best Test figures) was not re-checked; each is labelled accordingly.
- **ICC 2022 nomination figures** (735 runs, 25 wickets in 24 matches) come from the ICC citation via search; Wikipedia separately gives 516 T20I runs in 2022. The two may cover different match sets; the ICC figure was used for the nomination line.
- **2026 T20 World Cup final placing** — Zimbabwe reached the Super 8 (Wikipedia); how the Super 8 ended was not confirmed.
- **Australia ODIs, Harare, September 2026** — only the first result (Australia by 59 runs) was found; the second and third results and Raza's scores are missing.
- **UAE ODI tri-series, October 2026** — the dossier infers Zimbabwe reached the 23 October final from Raza's "last ODI" date; the result and his figures were not found.
- **Worcestershire Blast 2026 returns**, **India's T20Is in Zimbabwe (July 2026)**, and the **Seattle Orcas (MLC)** stint — not verified; the MLC team is mentioned only as "profile exists".
- **PSL 2023 title** — the ESPNcricinfo snippet says "two PSL titles"; the 2025 title is verified in detail, the 2023 one rests on the snippet plus Wikipedia's 2023–25 team listing.
- **Zimbabwe cap numbers** (Test 89, ODI 116, T20I 37) — from the Wikipedia infobox only.

## Errors in sources, discarded

- Wikipedia's body text calls Raza "the youngest player to score a T20I fifty, at just over 17". He debuted at 27; this is a page error and was ignored.
- Wikipedia's body text gives a T20I debut of 5 November 2013 v Bangladesh; the infobox and cricket.com.au both give 11 May 2013 v Bangladesh, which fits the May 2013 tour timeline, so 11 May 2013 was used.
- Wikipedia's "first non-residential player to represent Zimbabwe" phrasing is unclear and was not repeated.
- Outlook India's article says 22 Tests but quotes Raza saying "15 or 16"; the table figure (22) is the Cricinfo-sourced one.
- cricket.com.au shows Test best bowling as 8/176, which is a match figure (BBM), not an innings figure; the dossier uses 7/113 for BBI.

## Assumptions made

- Identity: no other international cricketer named Sikandar Raza was found; the dossier assumes the user means the Zimbabwe all-rounder.
- The "stats as of 12 November 2026" stamp trusts Wikipedia's infobox footer. Because his last international was 1 November 2026 and cricket.com.au shows identical figures, the tables are treated as current.
- "Late 2023" for the captaincy appointment is inferred as noted above.
- Ratings are the author's judgement against the skill's anchored scale; where evidence was thin (fielding, leadership W/L) the score was kept at the "good international standard" band rather than inflated.
- No inline chart tool was used; the ratings table stands on its own, as the skill allows.

## Deviation from the skill

- The skill says to also save a copy to `profiles/sikandar-raza.md`. Per the task instructions, nothing was written there; the dossier exists only in this outputs folder.
