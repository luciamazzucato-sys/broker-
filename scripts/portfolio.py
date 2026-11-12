#!/usr/bin/env python3
"""Portfolio report: values in EUR, allocation, P/L, and Luxembourg 6-month holding flags.

Usage: python3 scripts/portfolio.py [path/to/holdings.csv] [--as-of YYYY-MM-DD]

Each CSV row is one purchase lot. fx_to_eur converts price_currency to EUR
(e.g. for USD, the EUR value of 1 USD). Cost is converted with the same rate, so
P/L is approximate when you bought at a different FX rate.
"""
import csv
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta


def add_months(d: date, months: int) -> date:
    y, m = divmod(d.month - 1 + months, 12)
    y += d.year
    m += 1
    # clamp day to month end
    for day in (d.day, 30, 29, 28):
        try:
            return date(y, m, day)
        except ValueError:
            continue
    raise ValueError(d)


def main(argv):
    path = "portfolio/holdings.csv"
    as_of = date.today()
    args = list(argv)
    if "--as-of" in args:
        i = args.index("--as-of")
        as_of = datetime.strptime(args[i + 1], "%Y-%m-%d").date()
        del args[i : i + 2]
    if args:
        path = args[0]

    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        print("No holdings found in", path)
        return 0

    lots = []
    for r in rows:
        qty = float(r["quantity"])
        fx = float(r.get("fx_to_eur") or 1.0)
        value = qty * float(r["last_price"]) * fx
        cost = qty * float(r["cost_per_unit"]) * fx
        buy = datetime.strptime(r["buy_date"], "%Y-%m-%d").date()
        exempt_from = add_months(buy, 6) + timedelta(days=1)
        lots.append({**r, "value": value, "cost": cost, "buy": buy, "exempt_from": exempt_from})

    total = sum(l["value"] for l in lots)
    total_cost = sum(l["cost"] for l in lots)

    print(f"# Portfolio report (as of {as_of.isoformat()})\n")
    print(f"Total value: EUR {total:,.2f} | Cost: EUR {total_cost:,.2f} | "
          f"P/L: EUR {total - total_cost:,.2f} ({(total / total_cost - 1) * 100 if total_cost else 0:+.1f}%)\n")

    print("## Positions\n")
    print("| Symbol | Name | Value EUR | Weight | P/L % | Bought | >6 months? |")
    print("|---|---|---:|---:|---:|---|---|")
    for l in sorted(lots, key=lambda x: -x["value"]):
        pl = (l["value"] / l["cost"] - 1) * 100 if l["cost"] else 0
        long_term = as_of >= l["exempt_from"]
        flag = "yes" if long_term else f"no, from {l['exempt_from'].isoformat()}"
        print(f"| {l['symbol']} | {l['name'][:40]} | {l['value']:,.2f} | "
              f"{l['value'] / total * 100:.1f}% | {pl:+.1f}% | {l['buy'].isoformat()} | {flag} |")

    for key, title in (("asset_class", "Asset class"), ("region", "Region"),
                       ("price_currency", "Trading currency"), ("type", "Instrument type")):
        groups = defaultdict(float)
        for l in lots:
            groups[(l.get(key) or "unknown").strip() or "unknown"] += l["value"]
        print(f"\n## By {title.lower()}\n")
        print(f"| {title} | Value EUR | Weight |")
        print("|---|---:|---:|")
        for k, v in sorted(groups.items(), key=lambda kv: -kv[1]):
            print(f"| {k} | {v:,.2f} | {v / total * 100:.1f}% |")

    short = [l for l in lots if as_of < l["exempt_from"] and l["value"] > l["cost"]]
    if short:
        gain = sum(l["value"] - l["cost"] for l in short)
        print("\n## Luxembourg holding-period note\n")
        print(f"{len(short)} lot(s) in profit held 6 months or less (unrealised gain EUR {gain:,.2f}). "
              "Selling now could create taxable speculative gains (if the year's total is at least EUR 500). "
              "Check reference/luxembourg-investing.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
