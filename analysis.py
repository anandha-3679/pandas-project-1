import pandas as pd

# Load dataset
df = pd.read_csv("data/dataset.csv")

print("\n===== BASIC INFO =====")
print(df.info())

print("\n===== FIRST 10 ROWS =====")
print(df.head(10))

print("\n===== SHAPE =====")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DROP MISSING (OPTIONAL) =====")
df_clean = df.dropna()
print(df_clean.shape)

print("\n===== SUMMARY STATISTICS (NUMERIC) =====")
print(df.describe())

print("\n===== SUMMARY STATISTICS (OBJECT/CATEGORICAL) =====")
print(df.describe(include='object'))

print("\n===== UNIQUE VALUES PER COLUMN =====")
for col in df.columns:
    print(f"{col}: {df[col].nunique()}")

print("\n===== VALUE COUNTS FOR CATEGORICAL =====")
for col in df.select_dtypes(include='object'):
    print(f"\nColumn: {col}")
    print(df[col].value_counts())

print("\n===== CORRELATION (NUMERIC ONLY) =====")
print(df.corr(numeric_only=True))

print("\n===== SORTING EXAMPLES =====")
print(df.sort_values(by=df.columns[0]).head())

print("\n===== GROUPING EXAMPLE (IF POSSIBLE) =====")
for col in df.columns:
    if df[col].dtype == 'object':
        print(df.groupby(col).size())
        break

print("\n===== ANALYSIS COMPLETE =====")
