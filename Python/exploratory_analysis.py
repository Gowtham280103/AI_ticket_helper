import pandas as pd
import numpy as np

df = pd.read_csv("Dataset/cleaned_dataset/cleaned_issues.csv")

resolution_time = df["resolution_time_hours"].dropna()

print("Mean:", np.mean(resolution_time), "hours")
print("Median:", np.median(resolution_time), "hours")
print("Minimum:", np.min(resolution_time), "hours")
print("Maximum:", np.max(resolution_time), "hours")
print("Standard Deviation:", np.std(resolution_time), "hours")

print("\nTickets by Priority")
print(df["issue_priority"].value_counts())

print("\nTickets by Issue Type")
print(df["issue_type"].value_counts())

print("\nTop Projects")
print(df["issue_proj"].value_counts().head(15))

print("\nResolution Time by Priority")
print(
    df.groupby("issue_priority")["resolution_time_hours"]
    .agg(["count", "mean", "median"])
    .sort_values("mean")
)

print("\nResolution Time by Issue Type")
print(
    df.groupby("issue_type")["resolution_time_hours"]
    .agg(["count", "mean", "median"])
    .sort_values("mean")
)
