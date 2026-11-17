# Sources for cricketer research

Which site holds which fact, how to reach it, and what each one gets wrong. Read this before searching so the first search is the right one.

## What can actually be fetched (observed in testing, Nov 2026)

The most authoritative statistics sites refuse automated fetching. Trying them repeatedly wastes the research budget, so plan around it from the start.

| Site | Fetch | How to use it |
|---|---|---|
| Wikipedia player pages and list pages | Works | Main route to career tables. The infobox cites ESPNcricinfo and dates the snapshot. |
| cricket.com.au player profiles (`cricket.com.au/players/...`) | Works | Career tables for men's and women's internationals and Australian domestic and franchise cricket. Good cross-check for any player, not only Australians. |
| cricketweb.net StatsSpider | Works | Per-format batting, bowling and fielding tables for men's internationals. |
| Wisden, ICC news articles, national board and franchise sites | Mostly work | Records, awards, rankings updates, injuries, squads. |
| ESPNcricinfo profiles and Statsguru | Blocked (403) | Read through search-result snippets. Still the authority when snippets show a figure. |
| HowSTAT | Blocked (403) | Search snippets only. |
| Cricbuzz | Blocked | Search snippets only. |
| ICC rankings pages | Render dynamically, empty when fetched | Use news reports of the weekly rankings update, which give the points and the date. |

Try a blocked site once in case access has changed; if it fails, move on. Do not use shell tools to get around a block.

A practical sequence for most players:

1. Search `"<full name>" cricketer` to pin down identity and find the Wikipedia and cricket.com.au pages.
2. Fetch the Wikipedia page for the infobox tables and narrative, and note the infobox's "as of" date.
3. Fetch the cricket.com.au profile (or cricketweb.net for men's internationals) and cross-check the headline numbers.
4. For anything since the infobox date, search news for recent series and add the deltas.
5. Use ESPNcricinfo and HowSTAT search snippets to confirm records and splits.

## Primary sources, in order of authority

### ESPNcricinfo — the reference for identity and statistics
- Profile: `https://www.espncricinfo.com/cricketers/<name-slug>-<id>` (search `site:espncricinfo.com <player name>` to find the id).
- The profile page carries full name, birth date and place, batting and bowling style, teams, debut matches per format, and the career summary tables for every format, including domestic (First-class, List A, T20).
- Statistics update after every match, so this is the page to stamp the "as of" date from.
- Pitfall: the pages refuse automated fetching. Use search-result snippets for figures and the Wikipedia infobox, which reproduces ESPNcricinfo's tables with a date.
- Statsguru (`stats.espncricinfo.com`) holds the splits: career by year, home versus away, as captain, against a given opponent. It is also blocked, so search for news articles that quote a Statsguru split, and prefer the most recent one.

### Wikipedia — biography and a second source for headline figures
- The infobox lists international debuts, teams with years, and a career statistics table with a "source: ESPNcricinfo, as of <date>" footer. Check that footer date; infoboxes for less prominent players can be months stale.
- Good for career narrative, captaincy spells, awards, controversies with citations, and name variants.
- Pitfall: for shared names, the disambiguation page is the quickest way to see every cricketer of that name with country and era.

### HowSTAT (`howstat.com`) — men's international statistics
- Blocks automated fetching. Its search snippets still show per-format summaries, year-by-year and opponent-by-opponent breakdowns, and milestone lists.
- Covers men's Tests, ODIs and T20Is, and the IPL. Does not cover women's cricket or most other domestic cricket.

### ICC (`icc-cricket.com`)
- Current player rankings for batting, bowling and all-rounders in each format, men's and women's. The rankings pages render dynamically and come back empty when fetched, so take the ranking and points from a dated news report of the weekly update.
- ICC awards (Cricketer of the Year, format-specific awards, Emerging Player) with year.

### CricketArchive (`cricketarchive.com`)
- The deepest record of domestic and historical cricket, including scorecards from the 18th century on and minor-county, club and women's matches. Subscription-only; search snippets still confirm existence and dates.

### Cricbuzz
- Player profiles with career stats and recent match-by-match performances. Blocks automated fetching; search snippets and match reports from other outlets cover recent form.

## Women's cricket
- ESPNcricinfo profiles cover women's internationals with the same table structure; the Wikipedia infobox usually carries the figures.
- National board sites (cricket.com.au, ecb.co.uk, bcci.tv, cricketsouthafrica, nzc.nz) carry contract lists, squad news and injury updates.
- Franchise stats: WPL via iplt20.com's sister site (wplt20.com), WBBL via cricket.com.au, The Hundred via ecb.co.uk. ESPNcricinfo's series pages hold the per-tournament tables.
- Pitfall: historic women's Test and ODI records are incomplete on some aggregators. If a cell is missing, say so rather than estimate.

## Associate nations and historic players
- Associate players (Netherlands, Scotland, Namibia, USA, Nepal, UAE, Oman, and others): ESPNcricinfo and the ICC list their T20I and ODI records; HowSTAT covers them once they have international matches. Domestic careers are often in CricketArchive only.
- Historic players (pre-1970): the ESPNcricinfo profile text is usually a reproduced Wisden obituary or Cricketer of the Year citation, and is the best single source for style and career arc. Wisden Almanack archives (`wisdenalmanack.com`) and the Wisden obituary are authoritative on dates.
- Pitfall: for pre-1970 players, "ODI" and "T20I" rows do not exist; present Tests and First-class only.

## Franchise leagues
- IPL: `iplt20.com` official stats; ESPNcricinfo series pages; HowSTAT's IPL section.
- BBL and WBBL: cricket.com.au. PSL: `psl-t20.com`. CPL: `cplt20.com`. SA20: `sa20.co.za`. The Hundred: ecb.co.uk. ILT20: `ilt20.co`. MLC: `majorleaguecricket.com`.
- Auction prices and contracts are reported by ESPNcricinfo and Cricbuzz news; date them, since they change yearly.

## What each number means (so tables are labelled correctly)
- **Tests / ODIs / T20Is** — international matches only.
- **First-class** — includes Tests plus all multi-day domestic cricket (County Championship, Ranji Trophy, Sheffield Shield, and so on).
- **List A** — includes ODIs plus domestic one-day cricket.
- **T20 (all)** — includes T20Is plus every franchise and domestic T20. This is the row that gets mislabelled as T20I most often.
- **Avg** — batting average is runs per dismissal; bowling average is runs conceded per wicket.
- **SR** — batting strike rate is runs per 100 balls; bowling strike rate is balls per wicket. Label which one the table shows.
- **Econ** — runs conceded per over.
- **BBI / BBM** — best bowling in an innings / in a match.

## Search patterns that work
- `"<full name>" site:espncricinfo.com` — profile and id.
- `"<full name>" cricketer born` — disambiguation when a surname is shared.
- `<name> captaincy record Tests won` — then confirm on Statsguru or HowSTAT.
- `<name> fastest 100 wickets record still stands` — checking whether a record has been overtaken; confirm against the current record list, not the article.
- `<name> injury OR contract OR retirement <current year>` — for the recent context section on active players.
