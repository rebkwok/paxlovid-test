import pandas as pd

df = pd.read_feather("output/dataset.arrow")
df.drop("patient_id", axis=1, inplace=True)
total_by_month = df.sum()
total_by_month.to_csv("output/count.csv", index=True, index_label="Month", header=["Total Prescriptions"])
