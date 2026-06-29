import pandas as pd

df = pd.read_csv("netflix_titles.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)
print(df.duplicated().sum())
df.columns = df.columns.str.lower().str.replace(" ", "_")
print(df.columns)
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
print(df.dtypes)
df = df.dropna()
print(df.isnull().sum())

df.to_csv("cleaned_netflix.csv", index=False)
print("Dataset cleaned successfully")