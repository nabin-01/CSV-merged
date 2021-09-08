import glob
import os
import pandas as pd

merged_df = pd.concat([pd.read_csv(csv_file, index_col=0, header=0) for csv_file in glob.glob(
    os.path.join("CSV files/", "*.csv"))], axis=0, ignore_index=True)

merged_df.to_csv("merged.csv")
