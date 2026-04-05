import pandas as pd
import numpy as np
import yfinance as yf

# ------------ Load the data from raw imports ------------ 
crsp = pd.read_csv('data/wrds_data.csv') 
hmi = pd.read_excel('data/hmi.xls', header=None) 
treasury = pd.read_csv('data/10_year_treasury.csv') 
compustat = pd.read_csv('data/compustat.csv')

# ------------  Data Cleaning and Aggregation ------------ 
# HMI: reshaping
data_start_idx = hmi[hmi[0] == 1985].index[0]
hmi = hmi.iloc[data_start_idx:].reset_index(drop=True)
hmi.columns = ['Year', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
hmi['Year'] = hmi['Year'].astype(int)
hmi = hmi.melt(id_vars=['Year'], var_name='Month', value_name='HMI') # row per year -> row per month per year
hmi = hmi.sort_values(['Year', 'Month']).reset_index(drop=True)
hmi['HMI_lag1'] = hmi['HMI'].shift(1)
hmi = hmi.dropna(subset=['HMI_lag1']).reset_index(drop=True)

# FRED data; aggregating dailyt to monthly
treasury['date'] = pd.to_datetime(treasury['observation_date'], format='%Y-%m-%d')
treasury['Month'] = treasury['date'].dt.month
treasury['Year'] = treasury['date'].dt.year
treasury = treasury.groupby(['Year', 'Month'])['DGS10'].mean().reset_index() # from daily to monthly

# Compustat data; calculating ratios
compustat = compustat[compustat['indfmt'] == 'INDL'].copy() # to avoid duplicates
compustat['debt_to_assets'] = compustat['lt'] / compustat['at'] # Leverage: Total Liabilities / Total Assets
compustat['asset_growth'] = compustat.groupby('tic')['at'].pct_change() # Asset Growth: (Total Assets_t - Total Assets_{t-1}) / Total Assets_{t-1} 
compustat['log_assets'] = np.log(compustat['at']) # Size: log(Total Assets)
compustat['datadate'] = pd.to_datetime(compustat['datadate'], format='%Y-%m-%d')
compustat['Year'] = compustat['datadate'].dt.year
compustat = compustat[['tic', 'Year', 'debt_to_assets', 'asset_growth', 'log_assets']]

# REIT Data
treatment_tickers = ['ESS', 'UDR', 'MAA', 'CPT']
control_tickers = ['AMT', 'EQUIX', 'PLD']
crsp = crsp[crsp['TICKER'].isin(treatment_tickers + control_tickers)].copy()
crsp['date'] = pd.to_datetime(crsp['date'])
crsp['Month'] = crsp['date'].dt.month
crsp['Year'] = crsp['date'].dt.year
crsp['RET'] = pd.to_numeric(crsp['RET'], errors='coerce')
crsp['PRC'] = pd.to_numeric(crsp['PRC'], errors='coerce')
crsp = crsp[(crsp['date'] >= '2000-08-01') & (crsp['date'] <= '2024-12-31')].copy()
crsp = crsp.dropna(subset=['RET', 'PRC']).copy()
# Amihud (2002): ILLIQ = |R| / (|PRC| * VOL); NaN on no-trade days (VOL=0 or approx 0)
# so they are excluded from the monthly mean but still contribute to the return compounding
crsp['illiq_daily'] = np.where(
    crsp['VOL'] > 0,
    crsp['RET'].abs() / (crsp['PRC'].abs() * crsp['VOL']),
    np.nan
)
def calculate_monthly_ret(series):
    return (series + 1).prod() - 1
df_monthly = crsp.groupby(['TICKER', 'Year', 'Month']).agg({
    'illiq_daily': 'mean',
    'RET': calculate_monthly_ret,    
    'VOL': 'sum'                     
}).reset_index()
df_monthly.rename(columns={'RET': 'monthly_ret', 'illiq_daily': 'illiq_avg'}, inplace=True)

# Pull VIX data
today = pd.to_datetime('today').strftime('%Y-%m-%d')
vix = yf.download('^VIX', start='1990-01-01', end=today, interval='1d', progress=False)
if isinstance(vix.columns, pd.MultiIndex):
    vix.columns = ['_'.join(map(str, c)) for c in vix.columns]
close_col = next((c for c in vix.columns if 'close' in str(c).lower()), vix.select_dtypes(include='number').columns[0])
vix['Year'] = pd.to_datetime(vix.index).year
vix['Month'] = pd.to_datetime(vix.index).month
vix_monthly = vix.groupby(['Year','Month'], as_index=False)[close_col].mean().rename(columns={close_col: 'VIX'})
vix_monthly

# ------------ Merging and Final Clean up------------ 
df = df_monthly.merge(hmi[['Year', 'Month', 'HMI_lag1']], on=['Year', 'Month'], how='left')
df = df.merge(treasury, on=['Year', 'Month'], how='left')
df = df.merge(vix_monthly, on=['Year', 'Month'], how='left')
df = df.merge(compustat, left_on=['TICKER', 'Year'], right_on=['tic', 'Year'], how='left').drop(columns=['tic'])
df['log_illiq'] = np.log(df['illiq_avg'])
df = df.sort_values(['TICKER', 'Year', 'Month']).reset_index(drop=True)
df['treatment'] = df['TICKER'].apply(lambda x: 1 if x in treatment_tickers else (0 if x in control_tickers else np.nan))
df.columns = df.columns.str.lower()
df.to_csv('processed_data.csv', index=False)