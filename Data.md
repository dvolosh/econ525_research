# Data sources and query parameters

- **CRSP (WRDS)**
	- Market data (daily): returns, prices, volumes.
	- File: `data/wrds_data.csv`
	- Variables: divamt, bidlo, askhi, prc, vol, ret, bid, ask, retx, wwretd, wwretx, ewretd, ewretx, sprtrn
	- Source: https://wrds-www.wharton.upenn.edu/pages/get-data/center-research-security-prices-crsp/annual-update/stock-security-files/daily-stock-file/

- **Compustat (WRDS)**
	- Annual fundamentals for firm controls.
	- File: `data/compustat.csv`
	- Variables: tic, conml, act, at, lt, teq, mkvalt
	- Source: https://wrds-www.wharton.upenn.edu/pages/get-data/compustat-capital-iq-standard-poors/compustat/north-america-daily/fundamentals-annual/

- **NAHB Housing Market Index (HMI)**
	- National HMI (historic series).
	- Source: NAHB Table 2 — https://www.nahb.org/news-and-economics/housing-economics/indices/housing-market-index

- **DGS10 (FRED)**
	- 10‑Year Treasury yield.
	- File: `data/10_year_treasury.csv`
	- Source: https://fred.stlouisfed.org/series/DGS10

- **VIX**
	- CBOE VIX index pulled via `yfinance` in `data_processing.py`.

**Notes:**
- Not all variables were used in the final `df` produced by `data_processing.py`. Those were for experimenting, for example, `mkvalt` was frequently missing, so we used `at` (total assets) and `lt` (total liabilities) as to come up with control metrics instead.
- The time range was max, and we included many REIT tickers. Final time range and variable selection are documented in `data_investigation.ipynb` and `empiric_modeling.ipynb`.