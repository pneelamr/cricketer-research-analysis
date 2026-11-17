# Cricketer Research Analysis

A Claude Code skill that researches any cricketer and produces a source-verified dossier as a formatted PDF, plus the research made with it.

The skill covers men's and women's cricket, any country or era, and international, domestic and franchise careers. Name one player for a profile, or two or more for a head-to-head comparison that ends in a verdict.

## What's in this repository

| Path | Contents |
|---|---|
| `cricketer-research/` | The skill: instructions, source guide, comparison format, PDF builder and test cases |
| `profiles/` | Finished player dossiers, each as Markdown source plus PDF |
| `cricketer-research-workspace/` | Results from the first round of skill testing |

```
cricketer-research/
├── SKILL.md                      instructions Claude follows
├── references/
│   ├── sources.md                which sites hold which facts, and which block automated access
│   └── comparison-format.md      structure for head-to-head comparisons
├── scripts/
│   ├── make_pdf.sh               builds a PDF from a dossier's Markdown
│   └── md_to_pdf.py              the converter it runs
└── evals/                        four test cases with grading checks
```

## What a dossier contains

1. **Identity header:** full name, birth, teams, role, debuts in each format, status, and the date the statistics were checked.
2. **Career statistics:** batting and bowling tables for each format, with first-class, List A and T20 rows where they matter.
3. **Career arc:** the shape of the career, from debut to retirement or current standing.
4. **Angle section:** included when you say what the research is for, such as an article or a scouting report.
5. **Playing style:** technique, strengths and weaknesses, drawn from documented analysis.
6. **Summary table** of role, strengths, weaknesses and legacy.
7. **Attribute ratings out of 10**, each with a one-line reason, drawn as a bar chart in the PDF.
8. **Records and milestones**, each checked for whether it still stands.
9. **Recent form**, or what the player has done since retiring.
10. **Off-field context:** captaincy, sanctions, injuries.
11. **Numbered sources** with links and access dates.

Facts that sources disagree on are shown with both versions and their sources, not settled silently. Figures that cannot be confirmed are marked unconfirmed rather than filled in from memory.

## Install

The skill needs [Claude Code](https://claude.com/claude-code). Link the skill folder into your personal skills directory:

```bash
git clone https://github.com/pneelamr/cricketer-research-analysis.git
ln -s "$(pwd)/cricketer-research-analysis/cricketer-research" ~/.claude/skills/cricketer-research
```

Claude Code picks it up in the next session.

## Use

Ask in plain language. For example:

- `research Rashid Khan`
- `do a full profile on Ellyse Perry, with WBBL stats`
- `compare Virat Kohli and Steve Smith. Who's the better Test batter?`
- `I need a dossier on Sikandar Raza for an article on cricketers who play for a country they weren't born in`

Claude researches the player on the web, writes the dossier to `profiles/<first-last>.md` (comparisons go to `comparisons/<a>-vs-<b>.md`), builds the PDF next to it, and replies with a short summary and the PDF's location.

## Building a PDF by hand

To rebuild a PDF after editing its Markdown:

```bash
bash cricketer-research/scripts/make_pdf.sh profiles/sachin-tendulkar.md
bash cricketer-research/scripts/make_pdf.sh profiles/sachin-tendulkar.md --page-size a4
```

The default page size is US Letter. The script needs the reportlab Python library. It uses the system copy if one is installed; otherwise, on first use, it installs reportlab into a private environment under `~/.cache/cricketer-research`, leaving the system Python untouched.

## Profiles

| Player | Files | Statistics as of |
|---|---|---|
| Sachin Tendulkar | [PDF](profiles/sachin-tendulkar.pdf) · [Markdown](profiles/sachin-tendulkar.md) | Final career figures; records checked 17 November 2026 |

## Testing

The skill was tested on four prompts: a Tendulkar profile, an Ellyse Perry profile including the WBBL, a Kohli and Smith comparison, and a Sikandar Raza dossier for a themed article. Each prompt was run once with the skill and once without it, then graded against fixed checks.

| Test | With skill | Without skill |
|---|---|---|
| Sachin Tendulkar profile | 8 of 8 | 7 of 8 |
| Ellyse Perry, including the WBBL | 8 of 8 | 6 of 8 |
| Kohli vs Smith, better Test batter | 10 of 10 | 6 of 10 |
| Sikandar Raza, themed article | 8 of 8 | 6 of 8 |

The full outputs, grades and benchmark are in `cricketer-research-workspace/iteration-1/`. Open `review.html` there to browse them. The run times and token counts in the benchmark can't be compared between runs, because usage limits interrupted every run several times.

Those test dossiers came from the first version of the skill and have known gaps, listed in the grading files. The skill was revised afterwards: it now handles blocked sources, contested facts and totals that must add up, and adds the angle section. The checks in `cricketer-research/evals/` were tightened at the same time. The revised skill has not yet been re-run against them.

To re-run the tests with the Claude Code CLI, from the skill folder:

```bash
cd cricketer-research
claude plugin eval . --allow-tools Write,Edit,Bash,WebSearch,WebFetch
```

## Known limitations

- **Blocked statistics sites.** ESPNcricinfo, Statsguru, HowSTAT and Cricbuzz refuse automated access. The skill takes figures from Wikipedia, which reproduces ESPNcricinfo's tables with a date, cross-checks them against cricket.com.au and cricketweb.net, and reads the blocked sites through search results.
- **Current players go stale.** An active player's figures change every match. Each dossier states the date its numbers were checked.
- **Non-Latin text.** The PDF cannot lay out Urdu, Hindi or other non-Latin scripts correctly, and prints emoji as a question mark. The skill writes names in English spelling, and the PDF script warns if anything slips through.
- **Research quality depends on what is published.** Older women's and associate-nation records are often incomplete; the dossiers mark those gaps rather than estimate.

The dossiers are compiled by Claude from public sources. Check figures against the cited sources before publishing them.
