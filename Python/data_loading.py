import pandas as pd
import zipfile

zip_path = "Help Desk Tickets.zip"

with zipfile.ZipFile(zip_path, "r") as z:
    df = pd.read_csv(z.open("Help Desk Tickets/issues.csv"))

print("Dataset shape:", df.shape)
print(df.head())
