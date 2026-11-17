# User notes: Kohli vs Smith comparison

## Sources that failed to fetch

| Source | What happened | Effect |
|---|---|---|
| ESPNcricinfo player profiles (`/cricketers/virat-kohli-253802`, `/cricketers/steven-smith-267192`) | HTTP 403 (Akamai "Access Denied") | The primary statistics source in `references/sources.md` was unavailable, so headline tables come from the Wikipedia infoboxes, which cite ESPNcricinfo |
| ESPNcricinfo Statsguru home/away queries (player 253802, 267192) | Redirected 301 to stats.cricinfo.com, which returned HTTP 400 | Splits come from dated articles instead (see substitutions) |
| HowSTAT Test, ODI and T20I overview pages (PlayerID 3600 Kohli, 3756 Smith) | HTTP 403 (Cloudflare JavaScript challenge) | Only search-result excerpts used. Not retried, as instructed |
| Cricbuzz profiles | WebFetch cannot fetch from cricbuzz.com | Not used |
| ICC rankings pages (Test and ODI batting) | Page loaded, but the table is rendered by JavaScript and returned no data | Rankings taken from SportsDigest (3 Nov 2026) and PTI via Deccan Chronicle (11 Nov 2026) |
| cricket.com | DNS failure | Not used |
| CricketArchive (via the stats.acscricket.com redirect) | Subscription site; redirect not followed | Not used |

The session was interrupted by usage limits three times. Several planned lookups were never run:
- Kohli's Test captaincy record from a stats source
- Year-by-year Test averages for both players
- Smith's 2026 T20 World Cup appearances
- Results of the Nov 2026 New Zealand v India ODI series

An early attempt to download HowSTAT, ESPNcricinfo and Statsguru pages with curl into the session scratchpad was also blocked (403 and 400). Nothing from it is used. After the coordinator's instruction I made no further curl attempts.

## Substitutions

- **Headline Test, ODI and T20I figures.** Taken from the Wikipedia infoboxes (Kohli: ESPNcricinfo as of 4 Nov 2026; Smith: a 22 Oct 2026 snapshot) instead of ESPNcricinfo directly. Cross-checks:
  - **Kohli Tests:** HowSTAT snippet and SportsYaari both show 123 matches, 9,230 runs, 46.85. They match.
  - **Smith Tests:** CricketSky shows 127 matches, 11,003 runs, 55.29, which matches. The HowSTAT snippet is an older 125-Test snapshot: 10,920 runs at 56.00.
  - **Smith ODIs:** CricketSky shows 170 matches, 5,800 runs, 43.28. It matches.
- **Innings and strike-rate columns.** These come from SportsYaari (Kohli) and CricketSky (Smith), both undated.
  - SportsYaari's Kohli ODI row is stale (311 matches, 14,797 runs), so its ODI strike rate of 93.82 is labelled as a snapshot.
  - Kohli's Test and T20I careers are finished, so those strike rates (55.57 and 137.04) are final.
- **Test splits.** These come from news and statistics articles of different dates instead of Statsguru. Each split in the dossier carries its own date.
- **ICC rankings.** These come from news reports, not the ICC site.

## Figures I could not confirm

### Kohli

- **Captaincy record.** Matches, wins and losses as Test captain, and his batting average as captain, are not confirmed. The dossier says only "India's most successful Test captain", which is the ESPNcricinfo headline. I believe the record is 68 Tests and 40 wins, but that comes from memory and is deliberately left out.
- **Current ODI figures.** His ODI innings count and current ODI strike rate are unconfirmed. It is also unclear whether the 4 Nov 2026 infobox includes the 4 Nov Auckland ODI. The infobox gives his last ODI as 27 Sep 2026 v West Indies, which suggests it predates the New Zealand series.
- **New Zealand v India ODI series, 4–15 Nov 2026.** I found only two results:
  - 1st ODI, Auckland: India won by 5 wickets (DLS), Kohli 74 off 51.
  - 2nd ODI, Wellington: India won by 4 runs (DLS) to go 2–0 up. Kohli's score is unknown.

  Matches 3 to 5 and Kohli's other scores are unconfirmed. Search results also mixed in the January 2026 home series against New Zealand (New Zealand won 2–1; Kohli made 124 at Indore, his 54th ODI hundred). Treat any figure from that series as a different event.
- **Away record by country.**
  - **Australia:** 46.72 in one source, 46.73 in another; I used 46.72. An older snapshot ("six hundreds v Australia, five Down Under") predates his 2018–19 and 2024–25 hundreds in Perth. The final figure of 7 hundreds in Australia is used.
  - **South Africa:** one excerpt gives 891 runs at 49.50 in nine Tests in South Africa. Another gives 1,408 runs at 54.15 in 16 Tests, which is probably his record against South Africa home and away combined. I used 49.50 for "in South Africa". I could not tell whether it came from cricket365 or Sportskeeda.
- **The 2020–2024 slump.** The figures (an average of about 30.5 across the period, and yearly lows of 19.33 in 2020 and 24.53 in 2024) come from a cricket.one analysis, not Statsguru.
- **The 12-of-15 dismissal figure.** "12 of 15 Test dismissals in 2024 to balls outside off" comes from a column published around 6 Dec 2024, in the middle of the Border-Gavaskar series. I dated it from the ID in its URL. It does not cover the whole year.
- **Home and away split (ESPNcricinfo story 1485599).** The search summary said this article predated his final years. The arithmetic shows otherwise: home 4,336 plus away 4,774 is 120 short of his 9,230 total, and the two WTC finals account for those 120 runs. It is therefore treated as final career figures. The 120 WTC-final runs and the "17 Tests in England" reconciliation are my own derivations, not sourced directly.
- **Peak ICC Test rating.** I did not confirm the points figure. The dossier says only that it was below Smith's 947, which follows from 947 being second all-time.

### Smith

- **Test best bowling.** Wikipedia (citing ESPNcricinfo) gives 3/18; CricketSky gives 4/83. I used 3/18. CricketSky's figure is probably wrong or a different measure.
- **ODI retirement date.** The Wikipedia lead says he retired on 5 Mar 2025; the infobox gives his last ODI as 4 Mar 2025. The dossier says "Mar 2025" and gives the last ODI as 4 Mar.
- **T20I runs.** One outlet gave 872 runs in 67 T20Is. I used 1,094, which is supported by several sources and CricketSky.
- **2026 T20 World Cup.** I could not confirm whether he played any match. Reporting on his "cover" role and the criticism of his omission strongly suggests he did not.
- **Home average of 59.56 (NewsBytes, Aug 2026).** It may predate Australia's August 2026 home Tests against Bangladesh, including one in Darwin. I could not confirm whether he played those Tests.
- **Away average of 54.60.** This is from Feb 2025. Away and neutral Tests since then (for example the 2025 WTC final and the 2026 South Africa tour) are not reflected.
- **Average in England (58.51 in 19 Tests).** The figure is as of the 2023 Lord's Test. My count of Tests in England since then is an inference: the last three 2023 Ashes Tests and the 2025 WTC final. His current England average is unconfirmed.
- **Average in India (50.31 in 10 Tests).** The figure is from June 2023. I did not check whether Australia have toured India for Tests since.
- **Double hundreds (4).** This comes from the HowSTAT snippet at 125 Tests. It has to be unchanged, because he has scored only 83 runs in the two Tests since.
- **2025–26 Ashes average.** 57.20 in one source and "57" in another.
- **Current ranking points.** His rating in the 11 Nov ICC list is unconfirmed; only his position (fifth) was reported.

### Both players

- **"T20 (Domestic)" aggregator rows.** These are undated, and the label is the source's own. Going by the match counts, they are probably T20 (all matches) including T20Is. Because of that ambiguity they appear only in prose, not in the statistics tables.

## Assumptions

- **Which Steve Smith.** "Steve Smith" is taken as Steven Peter Devereux Smith of Australia, born 1989. No other Steve Smith fits a Test-batting comparison with Kohli. The dossier names Steven Barry Smith (1984) and Graeme Smith once as the ones ruled out.
- **Scope.** The request is read as a cross-format comparison with the verdict on Test batting. The ratings and the verdict are weighted toward the three Test-specific rows.
- **Final figures.** Kohli's Test and T20I figures are treated as final (he retired from Tests in May 2025 and from T20Is in June 2024).
- **Smith's figures are current.** His 22 Oct 2026 Test figures are treated as current: he missed the Cape Town Test (27–31 Oct), and his next scheduled Test is Perth on 9 Dec. I did not separately confirm that Australia have played no Test since Cape Town.
- **Ratings.** The ratings are my judgement, anchored to the skill's 10-point scale. The totals are 66 each; the Test-specific rows are 27–21 to Smith.
- **Unverified facts left out.** Some facts I believe are true could not be verified this session, so they are not in the dossier:
  - Kohli's 68 Tests and 40 wins as captain, and his Test average as captain
  - Smith's 2015 World Cup semi-final hundred and his 121 in the 2023 WTC final
  - Kohli's peak Test rating points
  - year-by-year averages for 2016–2019
- **Files.** As instructed, outputs were saved only to this folder, not to `profiles/` or `comparisons/` as the skill suggests. No chart was produced: the skill calls for one only when an inline chart tool is available, and the ratings table stands on its own in Markdown.
