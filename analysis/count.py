import pandas as pd

# Read df with counts per patient per month
totals_df = pd.read_feather("output/dataset.arrow")
totals_df.drop("patient_id", axis=1, inplace=True)

# New df with 1/0 to indicate patient has at least one prescription
exists_df = totals_df.copy()
exists_df[exists_df > 0] = 1

summed_by_month = pd.concat([totals_df.sum(), exists_df.sum()], axis=1)

summed_by_month.to_csv(
    "output/count.csv", 
    index=True, 
    index_label="Month", 
    header=["Total Prescriptions", "Total Patients"]
)

