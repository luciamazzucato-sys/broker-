---
name: investor-profile
description: Create or update the investor's profile (goals, horizon, risk tolerance, contributions, rules, target allocation) in profile/investor-profile.md. Use when the user wants to set up or change their investing goals or risk level, or when another skill finds TODO fields it needs.
---

# Investor profile

The profile at `profile/investor-profile.md` is the source of truth that every other skill reads.

## Steps

1. Read `profile/investor-profile.md`. List the fields that are `TODO` or that the user wants to change.
2. Interview the user **in small batches** (3–4 questions at a time, plain language, examples
   in EUR). Order: goal and horizon, then money (capital, monthly amount, emergency fund),
   then risk, then preferences and rules.
3. For risk, ask scenario questions rather than "low/medium/high" in the abstract:
   *"If your €10,000 portfolio fell to €6,500 in a year, would you sell, hold, or buy more?"*
   Map the answer to a max tolerable drawdown.
4. Check consistency and point out conflicts gently. Examples: a short horizon (<3 years)
   with high equity, no emergency fund, or one stock above the user's own max weight.
5. Propose a **target allocation** that fits the answers, as a range of 2–3 options
   (e.g. 100% global equity / 80-20 / 60-40). Explain the trade-off in one line each and
   let the user choose. Use broad, low-cost UCITS ETF building blocks; no specific
   products unless asked.
6. Write the updated file, set `_Last updated_` to today, and summarise the changes.

## Notes
- Never record account numbers, IBANs or logins.
- If the user lacks an emergency fund or has high-interest debt, mention it first: it
  usually beats investing.
