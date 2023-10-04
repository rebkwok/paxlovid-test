from pathlib import Path

import pandas as pd


output_path = Path("output")
input_files = output_path.glob("dataset*.arrow")

df = pd.concat((pd.read_feather(input_file) for input_file in input_files), ignore_index=True)
df.drop("patient_id", axis=1, inplace=True)

df.index = pd.to_datetime(df['date_treated'],format='%Y-%m-%d')
counts_by_month= df.groupby(pd.Grouper(freq="M")).count()
counts_by_month["month"] = counts_by_month.index.month
counts_by_month["year"] = counts_by_month.index.year
counts_by_month.rename(columns={"date_treated": "count"}, inplace=True)
counts_by_month.to_csv("output/count.csv", index=False)
