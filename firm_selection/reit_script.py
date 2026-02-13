import pandas as pd
import numpy as np

df = pd.read_csv("compustat_reit_firms.csv", dtype=str)
res = df['cusip'].unique()
cusip_string = " ".join(res.astype(str))
with open("reit_cusips.txt", "w") as f:
    f.write(cusip_string)