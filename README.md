Netflix Data Cleaning and Preprocessing

Overview

This project demonstrates the data cleaning and preprocessing of the Netflix Movies and TV Shows dataset using Python and Pandas. The dataset was cleaned by identifying missing values, removing duplicate records, standardizing column names, converting data types, and exporting the cleaned dataset for further analysis.

⸻

Objective

The objective of this project is to prepare raw data for analysis by performing essential data preprocessing techniques.

⸻

Tools Used

* Python
* Pandas
* Visual Studio Code

⸻

Dataset

Dataset: Netflix Movies and TV Shows

⸻

Data Cleaning Process

* Imported the dataset using Pandas.
* Displayed the first five rows using head().
* Examined dataset information using info().
* Identified missing values using isnull().sum().
* Removed duplicate records using drop_duplicates().
* Standardized column names by converting them to lowercase and replacing spaces with underscores.
* Converted the date_added column into datetime format.
* Removed rows containing missing values using dropna().
* Exported the cleaned dataset as cleaned_netflix.csv.

⸻

Project Files

task1.py
netflix_titles.csv
cleaned_netflix.csv
README.md

⸻

How to Run

1. Install Pandas.

pip install pandas

2. Run the Python file.

python task1.py

⸻

Output

The cleaned dataset is generated as:

cleaned_netflix.csv

⸻

Learning Outcomes

* Learned data cleaning using Pandas.
* Worked with missing values and duplicate records.
* Converted data types.
* Prepared a dataset for data analysis.

⸻

Author

Nandhana C K
