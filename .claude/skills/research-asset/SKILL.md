---
name: research-asset
description: Produce a one-page research note on a single stock or ETF (by ticker, ISIN or name) for a Luxembourg-based EUR investor, covering what it is, costs, risks, valuation, tax angle and fit with the investor profile. Use when the user asks "what do you think of X", "should I buy X", or "tell me about X".
---

# Research an asset

## Steps

1. Read `profile/investor-profile.md` and `portfolio/holdings.csv` (to judge fit and overlap).
2. Identify the instrument precisely: name, **ISIN**, the exchange and ticker best for a
   EUR investor, and trading currency. If a US-domiciled ETF is named, say it is probably not
   buyable under PRIIPs and find the closest **UCITS** equivalent.
3. Gather current facts with web search. Record the source and date for each figure.
4. Write the note using the template for the type below.
5. Save it to `reports/YYYY-MM-DD-research-<symbol>.md` and show a short summary in chat.

## ETF template
- **Snapshot:** index tracked, ISIN, domicile, replication (physical/synthetic), accumulating or
  distributing, TER, fund size (AUM), inception, EUR listing.
- **What you actually own:** number of holdings, top 10 weight, country/sector split, and
  currency exposure (not the same as trading currency).
- **Cost and efficiency:** TER plus tracking difference if available. Note the effect of
  domicile on withholding tax (see `reference/luxembourg-investing.md`).
- **Risks:** concentration, currency, liquidity/spread, and index methodology.
- **Alternatives:** 2–3 comparable UCITS ETFs (ISIN, TER, AUM).

## Stock template
- **Business:** what it sells, to whom, how it makes money, competitive position.
- **Financials (last 3–5 years):** revenue growth, margins, free cash flow, net debt, dividends/buybacks.
- **Valuation:** P/E, EV/EBITDA, FCF yield vs its own history and peers. State the assumptions behind them.
- **Bull case / bear case:** 3 points each.
- **Risks and catalysts:** next earnings date, regulation, key-person risk, currency.
- **Tax angle:** dividend withholding by country and the Luxembourg 50% dividend exemption
  eligibility (verify).

## Always end with
- **Fit with your profile:** how it fits your goal, horizon and risk level; how it overlaps
  with current holdings; what weight would be consistent with your max position rule.
- **Verdict framing:** "Fits / partially fits / doesn't fit your stated plan, because ...".
  No price targets presented as certainties.
- One line: *Research only, not personal financial or tax advice. Data as of <date>.*
