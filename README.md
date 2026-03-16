# HMI as a Leading Indicator for REIT Liquidity

## Project Overview
This research investigates whether homebuilder sentiment serves as an early warning signal for liquidity constraints in Real Estate Investment Trusts (REITs). Specifically, we test if the **NAHB/Wells Fargo Housing Market Index (HMI)**—a measure of single-family housing market health—can predict **Amihud Illiquidity (ILLIQ)** in the stock market with a one-month lead.

### The Core Hypothesis
> "Changes in homebuilder sentiment today predict liquidity 'dry-ups' in residential-backed REITs tomorrow."

**Significance:**
* **For Investors:** Provides a window to exit positions before transaction costs spike.
* **For REIT Managers:** Identifies optimal windows for SEOs (Seasoned Equity Offerings) or capital raising before market fluidity drops.

## Identification Strategy
To isolate the housing-specific information channel, we employ a treatment-control framework. By comparing residential REITs against non-residential peers, we can distinguish between housing-specific signals and general market volatility.

| Group | Description | Constituents |
| :--- | :--- | :--- |
| **Treatment** | Residential & Single-Family Rental REITs. Assets are directly tied to HMI drivers (mortgage rates, buyer traffic). | `ESS`, `AVB`, `INVH`, `UDR`, `MAA`, `CPT`, `AMH` |
| **Control** | Non-residential REITs. Acts as a placebo to ensure HMI isn't just reflecting general market fear. | `WELL`, `AMT`, `EQIX`, `PLD` |

---

## Econometric Specification
The analysis utilizes a **Pooled OLS regression** with log-transformed illiquidity to normalize the distribution of price impact metrics.

$$\log(ILLIQ_{i,t}) = \beta_0 + \beta_1(HMI_{t-1} \times Treat_i) + \beta_2 HMI_{t-1} + \beta_3 \log(ILLIQ_{i,t-1}) + \Gamma X_{i,t} + \delta Macro_t + \epsilon_{i,t}$$

### Variable Definitions
* **$\beta_1$ (Coefficient of Interest):** Measures the differential impact of lagged housing sentiment on the residential treatment group.
* **$X_{i,t}$ (Firm Controls):** A vector of annual fundamental controls (**Size**, **Leverage**, and **Asset Growth**) from Compustat. These act as "step" controls that remain constant throughout the fiscal year to account for structural changes like M&A.
* **$Macro_t$:** Monthly macroeconomic controls, including the **VIX** and **10-Year Treasury Yield**.
* **$\log(ILLIQ_{i,t-1})$:** An $AR(1)$ term to control for the inherent persistence in stock market liquidity levels.

---

## Success Criteria
The study rejects the Null Hypothesis ($H_0$: Housing sentiment does not differentially predict liquidity for residential REITs) if:

1.  **Primary Test:** The coefficient $\beta_1$ is **negative and statistically significant**. This indicates that improved sentiment predicts a subsequent reduction in illiquidity for residential REITs.
2.  **Robustness:** **Granger Causality** tests show a significant predictive relationship for the treatment group that is absent in the non-residential control group.