import pandas as pd

# Load dataset
df = pd.read_csv("raw_dataset.csv")

print("----- ORIGINAL DATASET -----")
print(df)

# 1. Check missing values
print("\n----- MISSING VALUES -----")
print(df.isnull().sum())

# 2. Remove duplicate records
df = df.drop_duplicates()

# 3. Remove extra spaces from column names
df.columns = df.columns.str.strip()

# 4. Remove extra spaces from text data
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# 5. Convert Age into numeric
if "Age" in df.columns:
    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

# 6. Convert Salary into numeric
if "Salary" in df.columns:
    df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

# 7. Convert Date into proper date format
if "Hire_Date" in df.columns:
    df["Hire_Date"] = pd.to_datetime(
        df["Hire_Date"], errors="coerce"
    )

# 8. Fill missing numeric values with median
for col in df.select_dtypes(include=["int64", "float64"]).columns:
    df[col] = df[col].fillna(df[col].median())

# 9. Fill missing text values
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].fillna("Unknown")

# 10. Standardize inconsistent Gender values
if "Gender" in df.columns:
    df["Gender"] = df["Gender"].replace({
        "M": "Male",
        "m": "Male",
        "F": "Female",
        "f": "Female"
    })

# 11. Check duplicates after cleaning
print("\n----- DUPLICATES AFTER CLEANING -----")
print(df.duplicated().sum())

# 12. Check missing values after cleaning
print("\n----- MISSING VALUES AFTER CLEANING -----")
print(df.isnull().sum())

# 13. Display cleaned dataset
print("\n----- CLEANED DATASET -----")
print(df)

# 14. Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("\nData cleaning completed successfully!")
print("File saved as: cleaned_dataset.csv")