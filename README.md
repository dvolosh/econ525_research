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
We utilize a **Panel Fixed Effects regression with a Difference-in-Differences (DiD) interaction term** as the primary model. The DiD interaction directly exploits our treatment/control design to isolate the housing-specific signal.

**Primary Model — Panel Fixed Effects DiD:**
$$ILLIQ_{i,t} = \alpha_i + \beta_1(HMI_{t-1} \times Treat_i) + \beta_2 HMI_{t-1} + \beta_3 ILLIQ_{i,t-1} + \gamma_1 VIX_t + \gamma_2 Treasury_t + \epsilon_{i,t}$$

| Term | Purpose |
| :--- | :--- |
| $\alpha_i$ | Firm fixed effects — absorbs time-invariant firm characteristics (size, leverage) |
| $\beta_1$ ($HMI_{t-1} \times Treat_i$) | **DiD coefficient of interest** — differential effect of HMI on residential REITs |
| $\beta_2$ | Baseline HMI effect shared across all REITs |
| $\beta_3$ | AR(1) term capturing ILLIQ persistence |

**The "Success" Criteria:**
We reject the Null Hypothesis ($H_0$: HMI does not differentially predict ILLIQ for residential REITs) if:
1. **Primary test:** $\beta_1$ is negative and statistically significant — higher homebuilder sentiment predicts lower illiquidity for the treatment group only.
2. **Robustness (Granger Causality by subsample):** Granger causality is significant for the treatment group but fails to reach significance for the control group, confirming the signal is housing-sector specific.