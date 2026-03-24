'''
Title: Netflix data wrangling project
Name: Sylvester Onyango Wanina
Cybershujaa ID: cs-da01-25087
Program: Data & AI-2026
Date: 2/10/2026

Description: This project focuses on cleaning, structuring and validating the
Netflix movies and TV shows datasets ...

'''

## 1. Import libraries and dependecies for the python environment
#Import libraries
import pandas as pd  #data processing, csv file I/O (eg. pd.read_csv)
import numpy as np #linear algebra
import os  #lets you interact with the operating system (e.g., navigate directories, list files, manage paths).
# os.listdir('/kaggle/input') #Lists all files and folders inside /kaggle/input

# !ls /kaggle/input/netflix-shows
#The ! prefix runs a shell command directly from a Jupyter/Kaggle notebook. 
#ls is a Linux command that lists the contents of the specified directory — in this case, a specific dataset folder called netflix-shows. 
#This would show the actual data files (likely a .csv file like netflix_titles.csv).


## # 2. Load the Netflix dataset from a CSV file and exploring its structure using pandas.
#Load the netflix dataset from the attached kaggle dataset
filepath = '/kaggle/input/datasets/shivamb/netflix-shows/netflix_titles.csv'

df = pd.read_csv(filepath)

#Overview of the dataset
df.info()
df #highlights the first and last 5 rows


## 3. Perform data discovery to assess data types, missing values, and quality issues
#1. Shape of the dataset
print('Dataset Shape (Rows, Columns):', df.shape)

#2. Column names
print('Column:\n', df.columns.tolist())

#3. Data types of each column
print('Data types:\n', df.dtypes)

#4. Missing values
print('\n:Missing Values per column:\n', df.isnull().sum())

#5. Duplicate rows
print("\nNumber of duplicate rows:", df.duplicated().sum())


## 4. Clean the dataset by handling duplicates, missing values, and formatting inconsistencies
# Fill missing values (safe version)
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Not Available')
df['country'] = df['country'].fillna('Unknown')

# Drop rows where rating or duration is missing
df.dropna(subset=['rating', 'duration'], inplace=True)

# Convert date_added safely - check if it's already datetime first
if df['date_added'].dtype == 'object':
    df['date_added'] = df['date_added'].str.strip()
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
else:
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Drop rows where date_added is NaT
df.dropna(subset=['date_added'], inplace=True)

# Standardize text columns
df['type'] = df['type'].str.strip().str.title()
df['rating'] = df['rating'].str.strip()

print("Cleaned shape:", df.shape)
print("\nMissing values after cleaning:\n", df.isnull().sum())


## 5. Transform and enrich the dataset using techniques like filtering, sorting, grouping, and feature extraction.
# Extract year, month, day from date_added
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month
df['month_name_added'] = df['date_added'].dt.month_name()

# Extract duration as integer
df['duration_int'] = df['duration'].str.extract(r'(\d+)').astype(float)

# Filter: Movies only
movies_df = df[df['type'] == 'Movie']
print("Number of Movies:", len(movies_df))

# Filter: TV Shows only
tv_df = df[df['type'] == 'TV Show']
print("Number of TV Shows:", len(tv_df))

# Sort by release_year descending
df_sorted = df.sort_values('release_year', ascending=False)
print("\nTop 5 most recent releases:")
print(df_sorted[['title', 'type', 'release_year']].head())

# Group by country - count of titles
country_counts = df.groupby('country')['title'].count().sort_values(ascending=False)
print("\nTop 10 countries by number of titles:")
print(country_counts.head(10))

# Group by rating
rating_counts = df.groupby('rating')['title'].count().sort_values(ascending=False)
print("\nContent by rating:")
print(rating_counts)

# Group by type and year added
type_year = df.groupby(['type', 'year_added'])['title'].count().reset_index()
type_year.columns = ['type', 'year_added', 'count']
print("\nContent added per year by type:")
print(type_year.tail(10))


## 6. Validate the final dataset by checking consistency, completeness, and logical accuracy.
# 1. Check final shape
print("\n1. Final Dataset Shape:")
print(f"   Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# 2. Check no nulls remain in critical columns
print("\n2. Null Check (Critical Columns):")
critical_cols = ['show_id', 'type', 'title', 'release_year', 'date_added', 'rating', 'duration']
print(df[critical_cols].isnull().sum())

# 3. Validate release_year is within sensible range
print("\n3. Release Year Range:")
print(f"   Min: {df['release_year'].min()}, Max: {df['release_year'].max()}")
invalid_years = df[(df['release_year'] < 1900) | (df['release_year'] > 2026)]
print(f"   Invalid release years: {len(invalid_years)}")

# 4. Validate 'type' only contains expected values
print("\n4. Unique Content Types:")
print(f"   {df['type'].unique()}")

# 5. Validate duration_int is positive
print("\n5. Duration Validation:")
invalid_duration = df[df['duration_int'] <= 0]
print(f"   Negative or zero durations: {len(invalid_duration)}")
print(f"   Min duration: {df['duration_int'].min()}")
print(f"   Max duration: {df['duration_int'].max()}")

# 6. Validate date_added is within sensible range
print("\n6. Date Added Range:")
print(f"   Earliest: {df['date_added'].min()}")
print(f"   Latest: {df['date_added'].max()}")
invalid_dates = df[df['date_added'].dt.year < 2008]
print(f"   Dates before Netflix launch (2008): {len(invalid_dates)}")

# 7. Check for any remaining whitespace in key text columns
print("\n7. Whitespace Check:")
for col in ['type', 'rating', 'title']:
    has_whitespace = df[col].str.startswith(' ').sum() + df[col].str.endswith(' ').sum()
    print(f"   {col}: {has_whitespace} entries with leading/trailing spaces")

# 8. Validate show_id uniqueness
print("\n8. Show ID Uniqueness:")
print(f"   Total rows: {len(df)}")
print(f"   Unique show_ids: {df['show_id'].nunique()}")
print(f"   Duplicates: {len(df) - df['show_id'].nunique()}")

# 9. Rating validity check
print("\n9. Valid Ratings Check:")
valid_ratings = ['G', 'PG', 'PG-13', 'R', 'NC-17', 'TV-Y', 'TV-Y7', 
                 'TV-Y7-FV', 'TV-G', 'TV-PG', 'TV-14', 'TV-MA', 'NR', 'UR']
invalid_ratings = df[~df['rating'].isin(valid_ratings)]
print(f"   Invalid/unexpected ratings: {len(invalid_ratings)}")
if len(invalid_ratings) > 0:
    print(f"   Values: {invalid_ratings['rating'].unique()}")

# 10. Final summary
print("VALIDATION SUMMARY")
print(f"Total records: {len(df)}")
print(f"No null values in critical columns: {df[critical_cols].isnull().sum().sum() == 0}")
print(f"No duplicate show_ids: {df['show_id'].nunique() == len(df)}")
print(f"Valid content types only: {set(df['type'].unique()) <= {'Movie', 'TV Show'}}")
print(f"Release years in valid range: {len(invalid_years) == 0}")


## 7. Export the final cleaned dataset to a .csv file ready for analysis or visualization
# 1. Final check before export
print("\n1. Pre-export Summary:")
print(f"   Shape: {df.shape}")
print(f"   Columns: {df.columns.tolist()}")

# 2. Export to CSV
output_path = '/kaggle/working/netflix_cleaned.csv'
df.to_csv(output_path, index=False)

# 3. Verify export was successful
import os
file_exists = os.path.exists(output_path)
file_size = os.path.getsize(output_path) / (1024 * 1024)  # Convert to MB

print("\n2. Export Status:")
print(f"   File saved: {file_exists}")
print(f"   File path: {output_path}")
print(f"   File size: {file_size:.2f} MB")

# 4. Re-read the exported file to confirm integrity
df_verify = pd.read_csv(output_path)
print("\n3. Verification (re-reading exported file):")
print(f"   Rows: {df_verify.shape[0]}")
print(f"   Columns: {df_verify.shape[1]}")
print(f"   Any nulls in critical columns: {df_verify[critical_cols].isnull().sum().sum()}")

# 5. Preview first 3 rows of exported file
print("\n4. Preview of Exported File (first 3 rows):")
print(df_verify.head(3).to_string())