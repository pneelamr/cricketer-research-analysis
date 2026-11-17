# User notes — Sachin Tendulkar dossier (run of 15–16 Nov 2026)

## Sources that failed to fetch

- **ESPNcricinfo** — profile page (`/cricketers/sachin-tendulkar-35320`), the legacy `/ci/content/player/35320.html` URL and the `stats.espncricinfo.com` redirect all returned HTTP 403. Identity and headline Test figures came only from the search-result snippet of the profile. The skill's preferred source for the "as of" tables was therefore unavailable; the ESPNcricinfo-sourced infobox on Wikipedia (dated 15 Nov 2013, i.e. final figures) and cricketweb.net StatsSpider were used instead.
- **HowSTAT** — all three player overview pages (Test, ODI, IPL; PlayerId 1735) returned 403. Per the coordinator's instruction they were not retried. Figures attributed to HowSTAT (Test avg 53.79, IPL avg 34.84, World Cup 2,278 runs at 56.95 in 45 matches) are taken from search snippets, not the pages.
- **Cricbuzz** — the search tool reports cricbuzz.com blocks the crawler; not used.
- **cricinfo.com legacy captains table** (`downloads.cricinfo.com/db/STATS/ODIS/...`) — redirected and was not followed (ESPNcricinfo hosts block fetches).
- **Statsguru** — not attempted given the ESPNcricinfo block.
- The WebSearch/WebFetch tools hit a usage limit twice mid-run; the run resumed after each reset. One batch of curl fallbacks via Bash could not be executed because the auto-mode safety classifier returned no verdict.

## Figures I could not confirm, or that conflict between sources

- **First-class and List A innings, not-outs and strike rate** — not available from any fetchable source; cells left blank in the table. Matches, runs, average, HS, 100s and 50s come from the Wikipedia infobox (ESPNcricinfo-sourced).
- **First-class and List A bowling figures** — omitted entirely (unverified).
- **T20 (all) row** (96 matches, 2,797 runs, 11 NO, avg 32.90, SR 121.08, 1 hundred, 16 fifties) — from secondary aggregators (crickettimes.com, sportsguff.com) that reproduce the ESPNcricinfo figures; not cross-checked against ESPNcricinfo itself.
- **IPL average** — HowSTAT snippet says 34.84; a Sportskeeda piece says "just under 36". 34.84 used (consistent with 2,334 runs and 11 not-outs). IPL fifties count not stated.
- **ODI captaincy split** — 73 matches, 23 won is agreed everywhere. The split 43 lost / 1 tied / 6 no-result comes from a Sportskeeda captains list and sums correctly to 73; Wikipedia's article text says "2 tied", which does not sum. Treat the tie/NR split as probable but unverified against Statsguru/HowSTAT.
- **Test Player-of-the-Match awards** — the all-format Wikipedia table says 14 (total 76); the Tests-only table on the same page and the Tendulkar article say 13. The 76 total is the widely quoted record figure and is used; the Test component is uncertain by one.
- **Test average** — ESPNcricinfo shows 53.78 (truncated); HowSTAT 53.79 (rounded). Both describe 15,921/296. The table uses 53.78 with a note.
- **Desert Storm 134** — the 143 on 22 April 1998 is fully documented. The ICC snippet confirms a 134 v Australia at Sharjah in the same event but did not state it was the final; the "final, two days later, on his 25th birthday" framing is from general knowledge and should be treated as unverified in this run.
- **241* at Sydney "abstaining from the cover drive"** — well-known anecdote; stated with "reportedly" because no fetched source in this run described it.
- **Net preparation against Warne in 1998** (facing leg-spin into roughs) — folklore, stated with "reportedly"; not sourced in this run.
- **"Passed Lara as leading Test run-scorer in October 2008"** — supported only by a Sportskeeda article title in search results; date and venue not independently confirmed.
- **ODI debut venue** (commonly given as Gujranwala) and **T20I debut venue** (Johannesburg) — not confirmed by a fetched source, so venues omitted; dates and opponents confirmed via Wikipedia.
- **Yorkshire 1992 figures** (16 first-class matches, 1,070 runs at 46.52) — from a fan blog only; omitted from the dossier. "First overseas player for Yorkshire" is stated in multiple sources and retained.
- **Hundreds on debut in Duleep and Irani Trophies** — secondary sources and blogs only; stated as "secondary sources credit him".
- **Record-status claims sourced from news reports rather than record pages:** Root passing most Test fifties (Sept 2026) and most fourth-innings Test runs (Jan 2026); Kohli passing most runs in ODI chases (4 Nov 2026); Root's current tally 14,278 from 169 Tests "as of November 2026"; Kohli's 86 international hundreds and 15,000 ODI runs (Sept 2026); Kohli 28,068 international runs (Jan 2026). None were checked against the live ESPNcricinfo records pages because those are blocked; they are flagged "reported" in the dossier. Kohli's figures will have moved since those reports.
- **Most Player of the Match awards** — "still stands" relies on the Wikipedia table updated 11 January 2026 (Tendulkar 76, Kohli 71). Kohli has played ODIs since; recheck before relying on this.
- **Ferrari import-duty controversy** — not found in the fetched Wikipedia extracts; only the gift itself is mentioned. Left unverified.
- **Arjun Tendulkar at Lucknow Super Giants (2026)** — from an aggregator snippet only.
- **Champions League T20 2011 title** with Mumbai Indians — not verified in this run and omitted; the 2013 CLT20 win is referenced in a fetched snippet and retained.
- **IML Season 2 postponement** — from a single Sportsdunia article of unknown date; an earlier report had the season going ahead 24 Oct–14 Nov 2026.
- **Playing-style text** — the ESPNcricinfo profile prose (the skill's preferred style source) was unavailable; style bullets draw on Wikipedia's technique section (quoted phrases), the Wisden/cricket.com.au Sharjah pieces, the Devdiscourse 2026 backlift remark, and the verified statistics.

## Assumptions made

- The user means Sachin Ramesh Tendulkar of India; Arjun Tendulkar ruled out.
- Because the player is retired, the dossier uses "final career figures" rather than a stats-as-of date, and replaces "Recent form" with "After playing", per the skill.
- No inline chart was rendered; the ratings table stands on its own. The outputs folder was treated as the only save destination (no copy written to `profiles/`), per the task instructions.
- Wikipedia infobox and cricketweb figures agree on every headline Test/ODI number, so no "newer source" arbitration was needed.
