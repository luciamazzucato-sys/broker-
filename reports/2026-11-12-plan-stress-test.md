# Plan Stress Test and Risk Assessment (2026-11-12)

_Research only, not personal financial or tax advice. Model: `scripts/montecarlo.py` (10,000 simulated market paths,
fat-tailed equity returns, real returns in today's euros). Assumptions: global equity 4.5% real/yr, vol 16%;
EUR bonds 0.75% real, vol 6%; S-Pension fee 1.25% (unverified); ETF fee 0.14%._

## Results

Total paid in over 13 years (incl. tax refunds): EUR 231,601

| Outcome at 65 | Capital | Spend-down income (25y, 2% real) |
|---|---:|---:|
| Bad (5th pct) | 176,069 | 746/month |
| Weak (25th) | 223,286 | 946/month |
| Median | 267,017 | 1,132/month |
| Good (75th) | 323,271 | 1,370/month |
| Very good (95th) | 447,091 | 1,895/month |

Chance capital at 65 < money paid in: 29.8%
Chance capital >= EUR 250k: 59.4%
Chance capital >= EUR 291k (old fixed-4% estimate): 37.3%
Worst fall from a peak during 13 years: median 5%, 1-in-20 paths 23%
Withdraw EUR 1,000/month for 25 yrs: money lasts in 63% of paths
Withdraw EUR 1,235/month for 25 yrs: money lasts in 39% of paths
Fixed monthly withdrawal that lasts 25 yrs in 90% of paths: ~EUR 715
Fixed monthly withdrawal that lasts 25 yrs in 95% of paths: ~EUR 627

## Stress tests (deterministic)

| Scenario | Capital at 65 | Spend-down income |
|---|---:|---:|
| Base: steady 4.5% equity / 0.75% bonds | 283,433 | 1,201/month |
| 2008-style crash at age 64 (equity -40%, bonds +5%) | 220,193 | 933/month |
| Crash at 64, then no recovery before 65 | 213,071 | 903/month |
| Lost decade: equity 0% real for 10 yrs, then normal | 236,923 | 1,004/month |
| Japan-style: equity -1% real every year | 207,441 | 879/month |
| Early crash at 53 (-40%), normal after | 255,598 | 1,083/month |

S-Pension fee sensitivity: at 2.2% instead of 1.25%, median capital falls by only ≈ €3,000 (the tax refund dominates).

## Correction to earlier figures
The earlier "€850–1,235/month" assumed a smooth 4% every year. With realistic ups and downs:
- **Median** investment income (spend over 25 yrs): **≈ €1,130/month**
- **Prudent** fixed withdrawal (lasts 25 yrs in 90% of paths): **≈ €715/month**
- Plan on **€700–1,100/month** from investments.

## Total retirement income (gross, today's euros)
| Source | Per month | Risk |
|---|---:|---|
| Luxembourg state pension (estimate) | €3,500–4,000 | Low: lifelong, indexed to prices and wages |
| Investments | €700–1,100 | Moderate: market-dependent |
| Foreign pensions | TODO | n/a |
| **Total** | **≈ €4,200–5,100** | Investments are ≈ 15–25% of total income |

## Risk register
| Risk | Size in euros / probability | Mitigation in the plan | Residual |
|---|---|---|---|
| Market crash near retirement | -40% equities at 64 means ≈ -€63k (capital €283k → €220k) | Glide path; state pension covers living costs, so no forced selling | Medium |
| Paper losses along the way | 1 path in 20 sees a ≥ 23% fall from peak (portfolio incl. new money); a 2008-type year on ~€150–200k equity ≈ -€60–80k | Automatic savings plan; rule "never stop" | Medium (behavioural) |
| Weak decade | Lost decade gives €237k; Japan-style gives €207k | Global diversification; bonds in last years | Medium |
| Real loss vs money paid in | ≈ 30% chance capital < €232k paid in (today's money) | Long-run equity premium; tax refund boost | Medium |
| Currency | ~75% non-EUR (≈ 63% USD). EUR +10% vs all means ≈ -7% portfolio | Diversified currencies; state pension is EUR | Low–medium |
| Concentration | US ≈ 63%; top-10 stocks ≈ 26% | Market-weight; optional ex-US tilt | Low–medium |
| Fees (S-Pension unknown) | 1.25% → 2.2% costs ≈ €3k | Check KID; accept ≤ 1.5% | Low |
| Job loss / illness before 65 | Contributions stop | Emergency fund; flexible plan | Medium (personal) |
| Tax-law change | 6-month exemption or 111bis could change | Review yearly | Low |
| Broker failure | Securities segregated (customer property) | Low cash at broker | Low |
| Longevity (living past 90) | Portfolio could run out on fixed withdrawals | State pension is lifelong; use flexible withdrawals | Low |

## Verdict
**Strong plan overall, with moderate investment risk.** Structure: low cost, diversified, tax-efficient (111bis, accumulating,
6-month rule), automatic, with a glide path. The large, lifelong state pension makes total retirement income
robust even in bad market scenarios (worst stress case still ≈ €4,400/month total gross).

## Improvements
1. **Flexible withdrawals in retirement** (e.g. take 4% of the current value each year, less after bad years) instead of a fixed amount, so the portfolio never runs out.
2. **Raise contributions with each salary increase** (+€100/month ≈ +€20k at 65).
3. **Cash/bond bucket**: from 63, hold ~2 years of planned withdrawals outside equities.
4. **Verify the open items**: S-Pension KID fees, TR savings-plan eligibility, official CNAP estimate, foreign pensions.
