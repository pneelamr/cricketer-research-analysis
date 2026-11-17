# User notes — Ellyse Perry dossier (research run 15–16 November 2026)

## Sources that failed to fetch, and what was used instead

| Source | Result | Replacement |
|---|---|---|
| ESPNcricinfo profile (`espncricinfo.com/cricketers/ellyse-perry-275487`, the `/ci/content/player/275487.html` form, `cricinfo.com`, `usa.cricinfo.com`, and the `espn.com/cricket/player` mirror) | HTTP 403 or redirect back to a blocked host, every variant | cricket.com.au player profile (Cricket Australia's official page) as the primary statistics source; Wikipedia infobox (ESPNcricinfo figures dated 10 Mar 2026) as the cross-check |
| Statsguru (`stats.espncricinfo.com`) | 301 redirect to `stats.cricinfo.com`; not followed, per the one-retry instruction and because that host returned 403 for the profile | No home/away, by-year or captaincy splits in the dossier |
| ESPNcricinfo records page (2025 World Cup, Australia batting) | HTTP 403 | Perry's 2025 World Cup aggregate left unconfirmed (see below) |
| Cricbuzz | Domain blocks the search crawler; no profile reachable | Not used |
| ICC rankings page (`icc-cricket.com/rankings/...`) | Page shell only; table loads dynamically | Wikipedia "ICC Women's Player Rankings" (ODI tables as of 2 Nov 2026, T20I as of 9 Nov 2026) |
| The Cricketer player profile (2020) | HTTP 403 | Style section built from ESPNcricinfo (2017, 2022), Wisden and cricket.com.au articles instead |
| Wisden player page (`wisden.com/players/ellyse-perry-59956`) | Fetched, but carries only news headlines, no stats or bio | Not used for figures |
| HowSTAT | Not attempted; does not cover women's cricket (per the skill's sources reference) | — |

## Figures I could not fully confirm

1. **International tables (Tests, ODIs, T20Is) are from a single statistics page** (cricket.com.au, fetched 15 Nov 2026). The cross-check is indirect: the Wikipedia/ESPNcricinfo snapshot of 10 Mar 2026 (15 Tests, 165 ODIs, 171 T20Is) plus the matches played since (3 ODIs v West Indies, 3 ODIs v Bangladesh; 3 T20Is v West Indies, 7 at the T20 World Cup, 3 v New Zealand including a no-result) gives exactly 15 / 171 / 184, and the Test row matches the snapshot exactly. Runs and averages for ODIs and T20Is therefore rest on cricket.com.au alone. Minor rounding differences exist (e.g. 4,691/95 computes to 49.38, the page shows 49.37); I kept the page's values.
2. **Balls bowled and bowling strike rates for internationals are converted** from the overs cricket.com.au publishes (343.3, 972.4, 415.5 overs). The Test conversion (2,061 balls) matches the ESPNcricinfo snapshot exactly, which supports the method. The WBBL balls cell is blank because the page shows overs as "329.23", which is not a valid overs figure; the Sixers page gives bowling SR 27.11, consistent with roughly 329.5 overs.
3. **WBBL figures (150 matches, 5,337 runs, 73 wickets)**: it is not certain whether the page included the Sixers' 15 Nov 2026 match v Melbourne Renegades. A cricket.com.au feature on 13 Nov said she had reached 150 matches, which would make the 15 Nov game her 151st; the page still showed 150 on 15/16 Nov. Treat the WBBL row as "as of 12–15 Nov 2026".
4. **List A row** is as of 10 Mar 2026 (ESPNcricinfo via Wikipedia) and excludes the six ODIs since. Innings, NO, SR and balls were not in the snapshot. No first-class row or combined T20 row is given because the only source for those (ESPNcricinfo) was unreachable.
5. **2025 ODI World Cup tournament aggregate**: not found from any reliable page. The dossier gives her semi-final 77 and the India group-game innings only. A news snippet citing ESPNcricinfo put her career World Cup record at 848 runs at 49.88 in 32 matches after the semi-final; not used in the dossier because it could not be checked.
6. **2026 T20 World Cup total**: 185 runs at 46.25 before the final is from cricket.com.au/ABC; "198 for the tournament" is my addition of her 13* in the final. Her bowling figures in the semi-final and final were not found (she appears not to have bowled in the final).
7. **WPL career**: 972 runs, 8 fifties, 6/15 and the 2024 Orange Cap figures are confirmed from the Wikipedia WPL records list and RCB. Match count (news reports say 25), career average (reports say 62–64.80) and strike rate (around 133) were only in news snippets, so they are stated as unconfirmed in the dossier.
8. **The Hundred career total**: only "over 500 runs" before 2026 (Edgbaston) plus 223 at 55.75 in 2026 (AAP via cricket.com.au). No exact career line.
9. **Women's Ashes aggregate**: "leading run-scorer and wicket-taker in Women's Ashes history" is well documented (January 2022). The figures quoted in the sources (1,552 runs; 68 then 71 wickets) are from different dates and are below her current totals after the 2023 and 2025 series. Stated as dated in the dossier.
10. **WBBL|04 season record**: cricket.com.au reports 777 runs; the Wikipedia records list shows 778. Both are given. The records list (accurate to the WBBL|11 final) still shows it as the season record.
11. **Test match best 9/70**: the figure is from cricket.com.au. Its attribution to the 2015 Canterbury Ashes Test rests on Wikipedia's narrative ("9-wicket match haul" in the 2015 Ashes) rather than a scorecard.
12. **Alana King's 7/18** superseding Perry's 7/22 as the best ODI figures by an Australian woman: King's 7/18 is confirmed from the 2025 World Cup statistics table; the opponent is not stated in the dossier because it was not in the fetched content.
13. **Missing innings in the recent-form section**: her scores in the 1st West Indies T20I, the three West Indies ODIs, the 1st Bangladesh ODI, the 2nd New Zealand T20I and the Sixers' 1 Nov, 8 Nov, 12 Nov and 15 Nov WBBL|12 matches were not in the fetched pages. Only the innings that were reported are listed.
14. **WPL 2027 availability** (RCB retention, September 2026) comes from a single IANS report, flagged as such.
15. **"Nine World Cups, first cricketer of either sex"** is from the Wikipedia 2026 T20 World Cup page; the count (2 ODI + 7 T20) checks out, but the "first of either sex" claim was not verified against a second source.
16. **ICC rankings**: her ODI batting rank (10th, 664) is from the Wikipedia rankings page dated 2 Nov 2026, not the ICC site itself. Absence from the all-rounder and T20I top tens is based on the same page.

## Assumptions made

- Identity: no disambiguation needed; "Ellyse Perry" refers to exactly one notable cricketer.
- The user asked for "all formats plus the WBBL", so the WBBL is treated as a full statistics row and given its own records and recent-form coverage; WPL and The Hundred are summarised in notes rather than full rows because no complete statistics table for them could be fetched.
- Batting positions ("No. 3/4 in Tests and ODIs, top three in T20s") are inferred from match reports (No. 3 in the 2023 Ashes and 2025 World Cup, opening in WBBL|12, early-innings scores in the NZ T20Is); no source states her current position explicitly for every format.
- Australia's current captain is given as Sophie Molineux for white-ball cricket (captain at the West Indies tour, the 2026 T20 World Cup and the NZ T20Is), with Tahlia McGrath standing in for the Bangladesh ODIs. Test captaincy after Alyssa Healy's retirement was not researched.
- Bowling-style description (outswing, classical action) relies on the cricket.com.au Hoggard article (2017) and Wisden's swing measurement (2019); no biomechanical analysis was found.
- Ratings are judgement calls on the skill's anchored scale; the evidence for each is in the "Why" column.
- No file was written to `profiles/`; the dossier was saved only to the outputs folder, as instructed. No inline chart was rendered.
