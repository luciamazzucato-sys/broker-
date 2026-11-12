#!/usr/bin/env python3
"""Monte Carlo + stress tests for the retirement plan (all values in today's euros, real returns).

Usage: python3 scripts/montecarlo.py [--sims 20000] [--seed 1] [--spension-fee 0.0125]

Assumptions (edit below, review yearly):
- Global equity: real geometric return ~4.5%/yr, volatility 16% (EUR investor, unhedged),
  fat tails via Student-t (df=5). Bonds (EUR govt): real ~0.75%/yr, vol 6%.
- ETF account: €20k start, €825/month + ~€1,880 yearly tax refund. Equity share 100% to age 58,
  then glides to 65% at 65 (via new money; annual rebalance approximates this).
- S-Pension: €4,500/yr, 75% equity to age 60, 50% to 63, 25% after; fee as given; ~15% tax at payout.
- Retirement phase: 25 years, balanced 50/50 portfolio, fixed real withdrawal.
"""
import argparse
import random
import statistics as st

EQ_MU, EQ_VOL = 0.045, 0.16      # geometric real return, volatility
BD_MU, BD_VOL = 0.0075, 0.06
ETF_FEE = 0.0014
YEARS = 13                        # age 52 -> 65
START_AGE = 52


def t_shock(rng, df=5):
    # Student-t scaled to unit variance
    z = rng.gauss(0, 1)
    chi = sum(rng.gauss(0, 1) ** 2 for _ in range(df))
    return z / (chi / df) ** 0.5 * ((df - 2) / df) ** 0.5


def draw(rng):
    eq = (1 + EQ_MU) * pow(2.718281828, EQ_VOL * t_shock(rng) - EQ_VOL ** 2 / 2) - 1
    bd = (1 + BD_MU) * pow(2.718281828, BD_VOL * rng.gauss(0, 1) - BD_VOL ** 2 / 2) - 1
    return eq, bd


def etf_equity_share(age):
    return 1.0 if age < 58 else max(0.65, 1.0 - (age - 57) * 0.05)


def sp_equity_share(age):
    return 0.75 if age < 60 else (0.50 if age < 63 else 0.25)


def accumulate(returns, sp_fee, monthly_etf=825, refund=1877, start=20000, sp_yearly=4500):
    etf, sp, peak, max_dd = start, 0.0, start, 0.0
    for y, (eq, bd) in enumerate(returns):
        age = START_AGE + y
        w = etf_equity_share(age)
        etf = (etf + monthly_etf * 6) * (1 + w * eq + (1 - w) * bd - ETF_FEE) + monthly_etf * 6 + refund
        v = sp_equity_share(age)
        sp = (sp + sp_yearly / 2) * (1 + v * eq + (1 - v) * bd - sp_fee) + sp_yearly / 2
        total = etf + sp
        if total > peak:
            peak = total
        max_dd = max(max_dd, (peak - total) / peak)
    return etf + sp * 0.85, max_dd


def drawdown_lasts(capital, monthly, rng, years=25):
    for _ in range(years):
        eq, bd = draw(rng)
        capital = (capital - monthly * 12) * (1 + 0.5 * eq + 0.5 * bd - ETF_FEE)
        if capital <= 0:
            return False
    return True


def pct(xs, p):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(p / 100 * len(xs)))]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sims", type=int, default=20000)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--spension-fee", type=float, default=0.0125)
    a = ap.parse_args()
    rng = random.Random(a.seed)

    finals, dds, lasts1000, lasts1235 = [], [], 0, 0
    for _ in range(a.sims):
        rets = [draw(rng) for _ in range(YEARS)]
        f, dd = accumulate(rets, a.spension_fee)
        finals.append(f)
        dds.append(dd)
        lasts1000 += drawdown_lasts(f, 1000, rng)
        lasts1235 += drawdown_lasts(f, 1235, rng)

    contributed = 20000 + YEARS * (825 * 12 + 1877 + 4500)
    print(f"# Monte Carlo ({a.sims} paths, S-Pension fee {a.spension_fee:.2%}), today's euros\n")
    print(f"Total paid in over 13 years (incl. tax refunds): EUR {contributed:,.0f}\n")
    print("| Outcome at 65 | Capital | Spend-down income (25y, 2% real) |")
    print("|---|---:|---:|")
    ann = (0.02 / 12) / (1 - (1 + 0.02 / 12) ** -300)
    for label, p in (("Bad (5th pct)", 5), ("Weak (25th)", 25), ("Median", 50),
                     ("Good (75th)", 75), ("Very good (95th)", 95)):
        v = pct(finals, p)
        print(f"| {label} | {v:,.0f} | {v * ann:,.0f}/month |")
    print(f"\nChance capital at 65 < money paid in: {sum(f < contributed for f in finals) / a.sims:.1%}")
    print(f"Chance capital >= EUR 250k: {sum(f >= 250000 for f in finals) / a.sims:.1%}")
    print(f"Chance capital >= EUR 291k (old fixed-4% estimate): {sum(f >= 291000 for f in finals) / a.sims:.1%}")
    print(f"Worst fall from a peak during 13 years: median {st.median(dds):.0%}, "
          f"1-in-20 paths {pct(dds, 95):.0%}")
    print(f"Withdraw EUR 1,000/month for 25 yrs: money lasts in {lasts1000 / a.sims:.0%} of paths")
    print(f"Withdraw EUR 1,235/month for 25 yrs: money lasts in {lasts1235 / a.sims:.0%} of paths")
    sample = finals[:2000]
    for target in (0.90, 0.95):
        lo, hi = 0, 3000
        while hi - lo > 10:
            mid = (lo + hi) / 2
            ok = sum(drawdown_lasts(f, mid, random.Random(i)) for i, f in enumerate(sample)) / len(sample)
            lo, hi = (mid, hi) if ok >= target else (lo, mid)
        print(f"Fixed monthly withdrawal that lasts 25 yrs in {target:.0%} of paths: ~EUR {lo:,.0f}")

    print("\n## Stress tests (deterministic)\n")
    base = [(EQ_MU, BD_MU)] * YEARS
    scen = {
        "Base: steady 4.5% equity / 0.75% bonds": base,
        "2008-style crash at age 64 (equity -40%, bonds +5%)": base[:12] + [(-0.40, 0.05)],
        "Crash at 64, then no recovery before 65": base[:11] + [(-0.40, 0.05), (0.0, 0.0)],
        "Lost decade: equity 0% real for 10 yrs, then normal": [(0.0, 0.01)] * 10 + base[10:],
        "Japan-style: equity -1% real every year": [(-0.01, 0.005)] * YEARS,
        "Early crash at 53 (-40%), normal after": [base[0]] + [(-0.40, 0.05)] + base[2:],
    }
    print("| Scenario | Capital at 65 | Spend-down income |")
    print("|---|---:|---:|")
    for name, r in scen.items():
        f, _ = accumulate(r, a.spension_fee)
        print(f"| {name} | {f:,.0f} | {f * ann:,.0f}/month |")


if __name__ == "__main__":
    main()
