Data Cleaning and Preprocessing using Pandas
Project Overview
This project focuses on cleaning and preprocessing the Netflix Movies and TV Shows dataset using Python and the Pandas library. The goal is to prepare raw data for analysis by handling missing values, removing duplicates, standardizing column names, converting data types, and exporting a cleaned dataset.

Objective
Identify and handle missing values.
Remove duplicate records.
Standardize column names.
Convert date columns to the correct data type.
Prepare the dataset for further analysis.
Dataset
Dataset Name: Netflix Movies and TV Shows

Technologies Used
Python 3
Pandas
Visual Studio Code
Data Cleaning Steps Performed
Imported the dataset using Pandas.
Displayed the first five rows using head().
Examined dataset information using info().
Checked for missing values using isnull().sum().
Checked and removed duplicate rows using drop_duplicates().
Renamed column headers to lowercase with underscores.
Converted the date_added column to datetime format.
Removed rows containing missing values using dropna().
Saved the cleaned dataset as cleaned_netflix.csv.
Files Included
task1.py – Python script for data cleaning.
netflix_titles.csv – Original dataset.
cleaned_netflix.csv – Cleaned dataset.
README.md – Project documentation.
How to Run the Project
Clone or download this repository.
Install Pandas:
pip install pandas
Run the Python script:
python task1.py
Output
The program generates a cleaned dataset named:

cleaned_netflix.csv
Learning Outcomes
Learned how to clean real-world datasets.
Gained hands-on experience with the Pandas library.
Understood handling of missing values and duplicate records.
Learned to convert data types and prepare datasets for analysis.
Author
Nandhana Rajeev