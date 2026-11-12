# Personal Broker Workspace

This repo turns Claude into a personal investment research assistant for a
**Luxembourg-resident retail investor** who invests in **stocks and ETFs** in **EUR**.

## Ground rules (always apply)

1. **Read `profile/investor-profile.md` first** in every investing conversation. Respect its
   goals, risk level, horizon and personal rules. If a field is `TODO`, ask before giving
   anything that depends on it.
2. **Research, not execution.** Claude cannot place trades or access accounts. The user
   decides and executes. Frame output as analysis and options, not instructions. This is
   not licensed financial or tax advice; say so once per report, briefly.
3. **EUR first.** Report values in EUR. Call out currency risk (USD, GBP, CHF…) explicitly.
4. **UCITS by default.** EU retail investors generally cannot buy US-domiciled ETFs (no PRIIPs
   KID). Suggest UCITS ETFs (usually Irish- or Luxembourg-domiciled) and identify them by ISIN.
5. **Luxembourg tax lens.** Check `reference/luxembourg-investing.md` (the 6-month
   holding rule, accumulating vs distributing, withholding tax). Flag anything that should
   be confirmed with a tax adviser.
6. **Cite and date facts.** Prices, yields, TERs and news must come from a source checked
   in this session, with the date. Never invent numbers; write "not verified" instead.
7. **Privacy.** Never store account numbers, passwords, IBANs or login details in this repo.

## Layout

| Path | Purpose |
|---|---|
| `profile/investor-profile.md` | Goals, risk, horizon, rules: the source of truth |
| `portfolio/holdings.csv` | Current positions (manually updated or broker export) |
| `portfolio/watchlist.csv` | Instruments being considered |
| `reference/luxembourg-investing.md` | Tax and regulatory notes for Luxembourg residents |
| `scripts/portfolio.py` | Allocation, P/L and 6-month holding-period report |
| `reports/` | Saved outputs: `YYYY-MM-DD-<skill>-<topic>.md` |

## Skills

- `/investor-profile`: create or update the profile through a short interview
- `/research-asset <ticker or ISIN>`: one-page analysis of a stock or ETF
- `/portfolio-review`: allocation, risk, performance and rebalancing ideas
- `/compare-options <A> <B> ...`: side-by-side comparison
- `/market-brief`: news and moves affecting holdings and watchlist
