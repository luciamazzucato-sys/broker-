# Investing from Luxembourg: Reference Notes

_Compiled 2026-11-12 from general knowledge. Tax law changes, so verify current rules with
the Administration des contributions directes (ACD, impotsdirects.public.lu) or a tax
adviser before acting. This is not tax advice._

## Product access (EU rules)
- **PRIIPs / KID:** EU retail investors can generally only buy funds and ETFs that publish a
  Key Information Document. Most **US-domiciled ETFs (e.g. VOO, SPY, QQQ) are not available**.
  Use **UCITS ETFs** instead, usually domiciled in Ireland (IE ISIN) or Luxembourg (LU ISIN).
- Individual US/EU **stocks** are not affected; they can be bought directly.
- Always identify ETFs by **ISIN**. The same fund trades under different tickers on
  different exchanges (Xetra, Euronext Amsterdam, LSE, Borsa Italiana, SIX).
- Prefer the **EUR-denominated listing** where liquid (often Xetra or Euronext). Note that
  the trading currency is not the same as currency exposure.

## Taxation of individuals (resident, private wealth)
- **Capital gains on securities held more than 6 months:** generally **tax-exempt** for
  private investors, unless it is a "substantial participation" (>10% of a company).
- **Speculative gains (held 6 months or less):** taxable at progressive income-tax rates,
  but only if total speculative gains for the year are **≥ €500**.
  -> The holding period matters: `scripts/portfolio.py` flags lots under 6 months.
- **Dividends:** taxed at progressive rates. A **50% exemption** may apply to dividends from
  fully taxable companies that are resident in Luxembourg, the EU, or a treaty country meeting
  the conditions. A small annual allowance also exists. Distributions from **funds/ETFs** are
  generally *not* eligible for the 50% exemption.
- **Accumulating ETFs:** Luxembourg does not tax reinvested fund income at the investor level.
  Combined with the 6-month rule, **accumulating UCITS ETFs held long-term are typically very
  tax-efficient** for Luxembourg residents.
- **Interest:** the 20% final withholding tax (RELIBI) applies to Lux-paid interest, and
  residents can opt in for certain EU-paid interest. This is mostly relevant to bond funds and cash.
- **Wealth tax:** none for individuals.

## Withholding tax drag inside ETFs (US equities)
- **Irish-domiciled** ETFs typically suffer **15%** US dividend withholding (US–Ireland treaty).
- **Luxembourg-domiciled** funds generally suffer **30%** on US dividends at fund level.
- So for US / global equity exposure, Irish-domiciled UCITS ETFs are usually slightly more
  efficient. The difference is roughly 0.2–0.3% per year on US dividends, so compare
  **tracking difference**, not just TER.
- Foreign withholding on **direct** dividends (e.g. US 15% with W-8BEN, others vary) may be
  creditable in Luxembourg up to treaty limits. Reclaim procedures vary by country.

## Retirement income: tax angle (verify)
- **Build-up phase:** accumulating UCITS ETFs reinvest dividends without investor-level tax.
- **Income phase, two ways to get cash:**
  - *Dividends / distributing ETFs:* taxed at progressive income-tax rates (fund distributions
    are generally not eligible for the 50% exemption).
  - *Selling a slice of shares held more than 6 months:* gains are generally tax-exempt for
    private investors. A planned "withdraw X% per year by selling" approach can therefore
    be more tax-efficient for a Luxembourg resident than living off dividends.
- **Art. 111bis private pension plan (prévoyance-vieillesse):** contributions are deductible up
  to **€4,500 per year** per taxpayer **from tax year 2026** (it was €3,200 for 2017–2025; source:
  impotsdirects.public.lu, checked 2026-11-12). The contract must run at least 10 years and be
  with an insurer or credit institution approved in Luxembourg. Payout starts no earlier
  than age 60, after at least 10 years of contributions. A partial lump sum is taxed at a
  reduced rate and the annuity portion is partly exempt. Products are limited (insurers and
  banks), and fees are often higher than ETFs. Compare the tax saving against the costs.
- **Employer supplementary pension** (if offered) is often the cheapest building block.

## Investor protection
- **Deposits:** FGDL guarantees up to **€100,000** per depositor per bank.
- **Securities (if a broker fails):** SIIL / investor compensation up to **€20,000**. Securities
  are normally held in segregated custody, but know which entity and country your broker uses.

## Reporting
- Keep trade confirmations, dividend statements and annual broker tax reports. Foreign
  brokers do not withhold Luxembourg tax, so taxable items go on the annual return
  (modèle 100).
