import pandas as pd

df = pd.read_csv("Dataset/raw_dataset/issues.csv")

selected_columns = [
    "id",
    "issue_proj",
    "issue_contr_count",
    "issue_type",
    "issue_priority",
    "issue_created",
    "issue_resolution_date",
    "issue_resolution",
    "issue_status",
    "issue_comments_count"
]

df = df[selected_columns].copy()

df["issue_created"] = pd.to_datetime(
    df["issue_created"],
    format="mixed",
    errors="coerce"
)

df["issue_resolution_date"] = pd.to_datetime(
    df["issue_resolution_date"],
    format="mixed",
    errors="coerce"
)

df["resolution_time_hours"] = (
    df["issue_resolution_date"] - df["issue_created"]
).dt.total_seconds() / 3600

df.loc[df["resolution_time_hours"] < 0, "resolution_time_hours"] = None

df["month"] = df["issue_created"].dt.month

df.to_csv(
    "Dataset/cleaned_dataset/cleaned_issues.csv",
    index=False
)

print("Cleaned dataset saved successfully.")
print(df.head())
