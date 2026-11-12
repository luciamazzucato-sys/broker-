---
name: market-brief
description: Write a short market brief covering news, price moves, earnings dates, dividends and macro events (ECB, Fed, EUR/USD) that affect the investor's holdings and watchlist. Use when the user asks "what's happening in the markets", "any news on my stocks", or for a weekly update.
---

# Market brief

## Steps

1. Read `portfolio/holdings.csv`, `portfolio/watchlist.csv` and the profile.
2. Use web search to collect events from the past 7 days, or since the last brief in `reports/`:
   - Material news per holding/watchlist item (earnings, guidance, M&A, index changes,
     fund closures or mergers for ETFs).
   - Weekly % move per holding, in EUR terms where possible.
   - Macro: ECB and Fed decisions, euro-area inflation, EUR/USD.
   - **Upcoming 2 weeks:** earnings dates, ex-dividend dates, central bank meetings.
3. Write the brief (one screen):
   - **Headline:** one sentence on what mattered most for *this* portfolio.
   - **Your holdings:** a bullet per item that had news; skip quiet ones.
   - **Macro:** 2–3 bullets.
   - **Coming up:** a dated list.
   - **Anything to act on?** Usually "no, stay the course". Flag only real triggers:
     a rebalancing band breached, a thesis broken, or a fund closing.
4. Save to `reports/YYYY-MM-DD-market-brief.md`.

Cite sources inline. Avoid hype and don't predict short-term prices.
