# HMI as a Leading Indicator for REIT Liquidity

## Project Overview
This research investigates whether homebuilder sentiment serves as an early warning signal for liquidity constraints in Real Estate Investment Trusts (REITs). Specifically, we test if the **NAHB/Wells Fargo Housing Market Index (HMI)**—a measure of single-family housing market health—can predict **Amihud Illiquidity (ILLIQ)** in the stock market with a one-month lead.

### The Core Hypothesis
> "Changes in homebuilder sentiment today predict liquidity 'dry-ups' in residential-backed REITs tomorrow."

**Significance:**
* **For Investors:** Provides a window to exit positions before transaction costs spike.
* **For REIT Managers:** Identifies optimal windows for SEOs (Seasoned Equity Offerings) or capital raising before market fluidity drops.

## Experimental Design
To isolate the housing-specific signal from general market noise, we employ a **Treatment vs. Control** framework using a Difference-in-Difference (DiD) approach.

| Group | Description | Constituents |
| :--- | :--- | :--- |
| **Treatment** | Residential & Single-Family Rental REITs. Assets are directly tied to HMI drivers (mortgage rates, buyer traffic). | `ESS`, `AVB`, `INVH`, `UDR`, `MAA`, `CPT`, `AMH` |
| **Control** | Non-residential REITs. Acts as a placebo to ensure HMI isn't just reflecting general market fear. | `WELL`, `AMT`, `EQIX`, `PLD` |

---

## Methodology & Econometrics
All data is aggregated at a **monthly (M)** frequency.

### Variables
* **Independent Variable ($X$):** Housing Market Index (HMI).
* **Dependent Variable ($Y$):** Amihud Illiquidity ($ILLIQ_{avg}$), calculated from daily returns and volume.
* **Macro Controls:** VIX (Market Volatility) and 10-Year Treasury Yield.

### Econometric Model
We utilize **Panel Vector Autoregression (Panel VAR)** and **Granger Causality** to prove the "leading" nature of the indicator.

**The Regression Equation:**
$$ILLIQ_{i,t} = \alpha + \beta_1 HMI_{t-1} + \beta_2 ILLIQ_{i,t-1} + \gamma Controls_t + \epsilon_{i,t}$$

**The "Success" Criteria:**
We reject the Null Hypothesis ($H_0$: Past values of HMI do not help predict current ILLIQ) if:
1.  **Treatment Group:** Granger Causality is statistically significant.
2.  **Control Group:** Granger Causality fails to reach significance (proving the HMI signal is sector-specific).