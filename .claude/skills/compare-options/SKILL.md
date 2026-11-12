---
name: compare-options
description: Compare two or more stocks, ETFs, brokers or strategies side by side for a Luxembourg-based EUR investor and recommend which fits the investor profile best. Use when the user asks "X vs Y", "which is better", or "which ETF should I pick for ...".
---

# Compare options

## Steps

1. Read `profile/investor-profile.md`.
2. Pin down each option precisely (ISIN for funds). Swap US-domiciled ETFs for UCITS equivalents.
3. Choose criteria for the type and gather data with sources and dates:
   - **ETFs:** index, TER, tracking difference, AUM, domicile, acc/dist, replication,
     number of holdings, top-10 weight, region/currency split, EUR listing and spread.
   - **Stocks:** growth, margins, FCF, debt, valuation multiples, dividend, main risks.
   - **Brokers:** availability to Luxembourg residents, fees for EU/US trades, FX fee,
     custody fee, savings plans, regulator and investor protection, tax reporting.
   - **Strategies (e.g. lump sum vs monthly investing, 1-ETF vs 3-ETF):** expected cost,
     risk, simplicity, and behaviour fit.
4. Present a comparison table, then **"Best fit for you: X"**, with 2–3 reasons tied to the
   profile and the main trade-off that would favour another option.
5. If options are close, say so; a small TER gap rarely matters more than staying invested.
6. Save to `reports/YYYY-MM-DD-compare-<topic>.md`.

End with: *Research only, not personal financial or tax advice. Data as of <date>.*
