# HMI as a Leading Indicator for REIT Liquidity

## Project Overview
This research investigates whether homebuilder sentiment serves as an early warning signal for liquidity constraints in Real Estate Investment Trusts (REITs). Specifically, we test if the **NAHB/Wells Fargo Housing Market Index (HMI)**—a measure of single-family housing market health—can predict **Amihud Illiquidity (ILLIQ)** in the stock market with a one-month lead.

### The Core Hypothesis
> "Changes in homebuilder sentiment today predict liquidity 'dry-ups' in residential-backed REITs tomorrow."

**Significance:**
* **For Investors:** Provides a window to exit positions before transaction costs spike.
* **For REIT Managers:** Identifies optimal windows for SEOs (Seasoned Equity Offerings) or capital raising before market fluidity drops.

## Identification Strategy
To isolate the housing-specific information channel, we employ a comparative framework. By examining residential REITs alongside non-residential peers, we can distinguish between housing-specific signals and broader commercial real estate or general market volatility.

| Group | Description | Constituents |
| :--- | :--- | :--- |
| **Residential REITs** | Residential & Single-Family Rental REITs. Assets are more directly tied to HMI drivers (mortgage rates, buyer traffic). | `ESS`, `UDR`, `MAA`, `CPT` |
| **Non-Residential REITs** | Other REITs. Included to ensure HMI isn't just reflecting general market fear or broad macroeconomic shifts. |  `AMT`, `EQIX`, `PLD` |

---

## Econometric Specification
The analysis utilizes a **Pooled OLS regression** and separate **Group-wise robust regressions** with log-transformed illiquidity to normalize the distribution of price impact metrics. We further test dynamic impacts via an **Impulse Response Function (IRF)**.

$$\log(ILLIQ_{i,t}) = \beta_0 + \beta_1(HMI_{t-1} \times Residential_i) + \beta_2 HMI_{t-1} + \beta_3 Residential_i + \beta_4 \log(ILLIQ_{i,t-1}) + \Gamma X_{i,t} + \delta Macro_t + \epsilon_{i,t}$$

### Variable Definitions
* **$\beta_1$ (Coefficient of Interest):** Measures the differential impact of lagged housing sentiment on Residential REITs vs. Non-Residential REITs.
* **$Residential_i$:** A dummy variable equal to 1 if the firm is a residential REIT, and 0 otherwise.
* **$X_{i,t}$ (Firm Controls):** A vector of annual fundamental controls (**Size**, **Leverage**, and **Asset Growth**) from Compustat. These act as "step" controls that remain constant throughout the fiscal year to account for structural changes like M&A.
* **$Macro_t$:** Monthly macroeconomic controls, including the **VIX** and **10-Year Treasury Yield**.
* **$\log(ILLIQ_{i,t-1})$:** An $AR(1)$ term to control for the inherent persistence in stock market liquidity levels.

---

## Key Results

- **HMI predicts illiquidity for both groups:** Lagged HMI is positive and statistically significant for Residential and Non-Residential REITs, indicating sector-wide increases in Amihud illiquidity following positive HMI shocks.
- **Different persistence:** IRF analysis shows the same-direction initial shock but different decay rates — residential REITs recover faster (shorter half-life) while non-residential REITs exhibit more persistent illiquidity (longer half-life).
