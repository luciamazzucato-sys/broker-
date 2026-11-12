---
name: portfolio-review
description: Review the investor's current portfolio (portfolio/holdings.csv) against their profile, covering allocation, concentration, currency and regional exposure, costs, performance, Luxembourg holding-period flags and rebalancing suggestions. Use when the user asks how their portfolio is doing, wants a check-up, or wants to rebalance or invest new money.
---

# Portfolio review

## Steps

1. Read `profile/investor-profile.md`. If the target allocation or risk fields are `TODO`,
   offer `/investor-profile` first, or continue with clearly stated assumptions.
2. Make sure holdings are current. Ask the user whether `portfolio/holdings.csv` is up to date.
   If they give a broker export, map it into the CSV columns (one row per purchase lot).
   Update `last_price` and `fx_to_eur` with web search when possible, and note the date.
3. Run `python3 scripts/portfolio.py` for the numbers.
4. Analyse:
   - **Allocation vs target:** drift per bucket in percentage points.
   - **Concentration:** single positions above the max weight; look-through overlap
     (e.g. MSCI World + S&P 500 + Apple means heavy US/Apple exposure).
   - **Currency:** actual underlying currency exposure, not trading currency.
   - **Costs:** weighted TER, with expensive positions flagged.
   - **Tax:** lots held 6 months or less (from the script). Prefer accumulating ETFs for
     long-term holdings, and use Irish domicile for US equity.
5. **Rebalancing ideas:** prefer directing **new contributions** to underweight buckets over
   selling (no transaction costs, no tax events). If selling, prefer lots held more than
   6 months. Show the EUR amounts per bucket.
6. Save to `reports/YYYY-MM-DD-portfolio-review.md`. In chat, give the top 3 findings and
   the suggested actions.

End with: *Research only, not personal financial or tax advice.*
