# 🎬 Netflix Data Wrangling Project

**Author:** Sylvester Onyango Wanina
**Cybershujaa ID:** cs-da01-25087
**Program:** Data & AI-2026
**Date:** 2/10/2026

---

## 📋 Project Description

This project focuses on cleaning, structuring, and validating the Netflix movies and TV shows dataset available on Kaggle. It demonstrates core **Data Wrangling** concepts using Python and pandas inside a **Kaggle Notebook** environment.

---

## 🌐 Dataset

- **Source:** [Netflix Movies and TV Shows – Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- **File:** `netflix_titles.csv`
- **Records:** 8,807 rows, 12 columns
- **Columns:** `show_id`, `type`, `title`, `director`, `cast`, `country`, `date_added`, `release_year`, `rating`, `duration`, `listed_in`, `description`

---

## ⚙️ Environment Requirements

> **⚠️ This project is designed to run exclusively on [Kaggle Notebooks](https://www.kaggle.com/code). Do NOT run it locally unless you manually download the dataset and adjust all file paths.**

### How to Set Up on Kaggle:

1. Go to [https://www.kaggle.com/datasets/shivamb/netflix-shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)
2. Click **"New Notebook"** to open the dataset directly in a Kaggle Notebook
3. Make sure the dataset is attached — it will be available at:
   ```
   /kaggle/input/netflix-shows/netflix_titles.csv
   ```
4. Your output files will be saved to:
   ```
   /kaggle/working/
   ```
5. Click **"Save & Run All (Commit)"** to execute the full notebook

---

## 📦 Libraries Used

```python
import pandas as pd   # Data processing and CSV file I/O
import numpy as np    # Linear algebra and numerical operations
import os             # Operating system interactions and file navigation
```

---

## 🎯 Project Objectives

### Objective 1 — Load & Explore the Dataset
- Load the Netflix CSV file using `pd.read_csv()`
- Explore structure using `df.info()`, `df.shape`, `df.head()`

### Objective 2 — Data Discovery
- Inspect column names and data types with `df.dtypes`
- Identify missing values using `df.isnull().sum()`
- Check for duplicate rows using `df.duplicated().sum()`

**Key findings:**
| Column | Missing Values |
|---|---|
| director | 2,634 |
| country | 831 |
| cast | 825 |
| date_added | 10 |
| rating | 4 |
| duration | 3 |

### Objective 3 — Clean the Dataset
- Fill missing values in `director`, `cast`, and `country`
- Drop rows with missing `rating`, `duration`, and `date_added`
- Convert `date_added` to datetime format
- Standardize text columns (strip whitespace, title case)

### Objective 4 — Transform & Enrich
- Extract `year_added`, `month_added`, `month_name_added` from `date_added`
- Extract numeric duration into a new `duration_int` column
- Filter Movies vs TV Shows separately
- Sort by `release_year`
- Group by `country`, `rating`, and `type` for trend analysis

### Objective 5 — Validate the Dataset
- Confirm zero nulls in all critical columns
- Validate `release_year` is within a sensible range (1900–2026)
- Verify `type` only contains `Movie` or `TV Show`
- Check `show_id` uniqueness
- Validate all ratings against standard Netflix rating values
- Confirm no leading/trailing whitespace in key columns

### Objective 6 — Export the Cleaned Dataset
- Export the final cleaned DataFrame to CSV
- Verify file existence, size, and integrity by re-reading it

**Output file:**
```
/kaggle/working/netflix_cleaned.csv
```

To download the output file from Kaggle:
1. Go to the **Output** tab on the right sidebar of your notebook
2. Find `netflix_cleaned.csv`
3. Click the **download icon**

---

## 📁 Project Structure

```
Netflix Data Wrangling/
│
├── notebook.ipynb          # Main Kaggle Notebook with all code
├── README.md               # Project documentation (this file)
│
├── input/                  # Auto-mounted by Kaggle (do not edit)
│   └── netflix_titles.csv
│
└── output/                 # Generated after running the notebook
    └── netflix_cleaned.csv
```

---

## ✅ Final Dataset Summary

| Metric | Value |
|---|---|
| Original rows | 8,807 |
| Cleaned rows | ~8,790 |
| Columns (original) | 12 |
| Columns (enriched) | 16 |
| Missing values remaining | 0 |
| Duplicate rows | 0 |

---

## 📌 Important Notes

- All file paths (`/kaggle/input/`, `/kaggle/working/`) are **Kaggle-specific** and will not work in a local Python environment without modification
- The `!ls` shell commands (prefixed with `!`) only work inside **Jupyter/Kaggle notebooks**
- If you encounter `FutureWarning` with `fillna(inplace=True)`, replace with `df['col'] = df['col'].fillna('value')` for pandas 3.0 compatibility
- Re-running cells multiple times may cause errors on `date_added` string operations — the notebook handles this with a dtype check

---

## 🔗 References

- [Kaggle Dataset – Netflix Shows by Shivam Bansal](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- [pandas Documentation](https://pandas.pydata.org/docs/)
- [Kaggle Notebooks Guide](https://www.kaggle.com/docs/notebooks)