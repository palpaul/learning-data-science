# pandas is a powerful library for data manipulation and analysis in Python. It provides data structures like DataFrame and Series, which allow for efficient handling of structured data. With pandas, you can easily perform operations such as filtering, grouping, and aggregating data, making it an essential tool for data scientists and analysts.  
#pandas library is used for data manipulation and analysis in Python. It provides data structures like DataFrame and Series, which allow for efficient handling of structured data. With pandas, you can easily perform operations such as filtering, grouping, and aggregating data, making it an essential tool for data scientists and analysts. 
#pandas deal with tabular data
#padnas is built on top of numpy, which provides support for large, multi-dimensional arrays and matrices. This allows pandas to efficiently handle and manipulate large datasets. Additionally, pandas integrates well with other libraries such as matplotlib for data visualization and scikit-learn for machine learning, making it a versatile tool for data analysis and modeling.    
#pandas is able to clean the data by handling missing values, removing duplicates, and performing data transformations. It also provides powerful tools for data visualization, allowing users to create various types of plots and charts to explore and communicate insights from their data. Overall, pandas is a fundamental library for anyone working with data in Python, offering a wide range of functionalities for data manipulation, analysis, and visualization.   


# openpyxl library is a Python library for reading and writing Excel files. It allows you to create, modify, and extract data from Excel spreadsheets. With openpyxl, you can perform various operations such as formatting cells, adding formulas, and creating charts. This library is particularly useful for automating tasks related to Excel, such as generating reports or processing large datasets. Whether you're working with .xlsx files or need to manipulate existing spreadsheets, openpyxl provides a convenient and efficient way to handle Excel files in Python.
# pandas is also used for reading and writing csv and Excel files, making it a powerful tool for data manipulation and analysis. With pandas, you can easily import data from Excel spreadsheets into DataFrames, allowing for efficient data cleaning, transformation, and analysis. Additionally, pandas provides functionality to export DataFrames back to Excel format, enabling seamless integration with Excel for reporting and sharing results. Whether you're working with small datasets or large spreadsheets, pandas offers a convenient and efficient way to handle Excel files in Python.    
from openpyxl import *



#pandas library
#from pandas import * or import pandas as pd
import pandas as pd


#pandas example
# Create a Series from a list
data = [10, 20, 30, 40, 50]
series = pd.Series(data)  # Create a Series from a list of numbers. The Series will have a default index starting from 0.   
# Display the Series 
print(series)



# pandas example
# Create a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data) # Create a DataFrame from a dictionary where the keys represent column names and the values are lists of data for each column. The resulting DataFrame will have three columns: 'Name', 'Age', and 'City', with corresponding data for each row.
# Display the DataFrame
print(df)
print(df['Name']) # Access the 'Name' column of the DataFrame, which will return a Series containing the names of the individuals.  
print(df.loc[0]) # Access the first row of the DataFrame using the .loc indexer, which will return a Series containing the data for the first individual (Alice) including their name, age, and city.
print(df.iloc[1]) # Access the second row of the DataFrame using the .iloc indexer, which will return a Series containing the data for the second individual (Bob) including their name, age, and city.
print(df[df['Age'] > 30]) # Filter the DataFrame to include only rows where the 'Age' column is greater than 30, which will return a new DataFrame containing only the individuals who are older than 30 (Charlie in this case).    
print(df.describe()) # Generate descriptive statistics for the DataFrame, which will provide summary information about the numerical columns (in this case, the 'Age' column) including count, mean, standard deviation, minimum, and maximum values.   
print(df.groupby('City')['Age'].mean()) # Group the DataFrame by the 'City' column and calculate the mean age for each city, which will return a Series with the average age of individuals in each city (New York, Los Angeles, and Chicago).  
print(df.sort_values('Age')) # Sort the DataFrame by the 'Age' column in ascending order, which will rearrange the rows based on the age of the individuals, with the youngest person appearing first and the oldest person appearing last.
print(df.sort_values('Age', ascending=False)) # Sort the DataFrame by the 'Age' column in descending order, which will rearrange the rows based on the age of the individuals, with the oldest person appearing first and the youngest person appearing last.   
print(df['Age'].mean()) # Calculate the mean (average) age of the individuals in the DataFrame, which will return a single value representing the average age of the group.
print(df['Age'].median()) # Calculate the median age of the individuals in the DataFrame, which will return a single value representing the middle age when the ages are sorted in order. If there is an even number of ages, it will return the average of the two middle values.
print(df['Age'].std()) # Calculate the standard deviation of the ages in the DataFrame
print(df['Age'].min()) # Calculate the minimum age in the DataFrame
print(df['Age'].max()) # Calculate the maximum age in the DataFrame
print(df['Age'].value_counts()) # Count the occurrences of each unique age in the 'Age' column of the DataFrame, which will return a Series with the age values as the index and their corresponding counts as the values.  
print(df['Age'].unique()) # Get the unique age values in the 'Age' column of the DataFrame, which will return an array of distinct ages present in the dataset. 
print(df['Age'].nunique()) # Count the number of unique age values in the 'Age' column of the DataFrame, which will return a single integer representing the count of distinct ages in the dataset. 
print(df['Age'].isnull()) # Check for missing values in the 'Age' column of the DataFrame, which will return a Series of boolean values indicating whether each age value is null (True) or not (False).
print(df['Age'].notnull()) # Check for non-missing values in the 'Age' column of the DataFrame, which will return a Series of boolean values indicating whether each age value is not null (True) or null (False).
print(df['Age'].fillna(df['Age'].mean())) # Fill any missing values in the 'Age' column of the DataFrame with the mean age, which will return a new Series where any null values in the 'Age' column are replaced with the average age calculated from the existing non-null values.
print(df['Age'].dropna()) # Remove any missing values from the 'Age' column of the DataFrame, which will return a new Series containing only the non-null age values, effectively filtering out any rows where the age is missing.  
print(df['Age'].interpolate()) # Interpolate missing values in the 'Age' column of the DataFrame, which will return a new Series where any null values in the 'Age' column are filled in using linear interpolation based on the existing non-null values. This method estimates the missing values by calculating a weighted average of the surrounding data points.
print(df['Age'].rolling(window=2).mean()) # Calculate the rolling mean of the 'Age' column in the DataFrame with a window size of 2, which will return a new Series where each value is the average of the current and previous age values. The first value will be NaN since there is no previous value to average with.
print(df.head()) # Display the first few rows of the DataFrame, which will return a new DataFrame containing the top 5 rows by default. This is useful for quickly inspecting the structure and contents of the DataFrame.
print(df.tail()) # Display the last few rows of the DataFrame, which will return a  new DataFrame containing the bottom 5 rows by default. This is useful for quickly inspecting the end of the DataFrame and checking for any patterns or anomalies in the data.
print(df.sample(3)) # Randomly sample 3 rows from the DataFrame, which will return a new DataFrame containing 3 randomly selected rows from the original DataFrame. This is useful for getting a quick look at different parts of the dataset without having to view the entire DataFrame.  
print(df.head(2)) # Display the first 2 rows of the DataFrame, which will return a new DataFrame containing only the top 2 rows. This is useful for quickly inspecting the structure and contents of the DataFrame when you only want to see a small sample of the data.
print(df.tail(2)) # Display the last 2 rows of the DataFrame, which will return a new DataFrame containing only the bottom 2 rows. This is useful for quickly inspecting the end of the DataFrame and checking for any patterns or anomalies in the data when you only want to see a small sample of the data.
print(df.shape) # Get the shape of the DataFrame, which will return a tuple representing the number of rows and columns in the DataFrame. This is useful for understanding the dimensions of the dataset.
print(df.info()) # Get a summary of the DataFrame, which will return information about the
print(df.size) # Get the total number of elements in the DataFrame, which will return a single integer representing the count of all values in the dataset.   

print(df.index) # Get the index of the DataFrame, which will return a RangeIndex object representing the row labels of the DataFrame. This is useful for understanding how the rows are indexed and for performing operations that involve row selection or manipulation.
print(df.columns) # Get the columns of the DataFrame, which will return an Index object representing the column labels of the DataFrame. This is useful for understanding the structure of the dataset and for performing operations that involve column selection or manipulation.
print(df.dtypes) # Get the data types of each column in the DataFrame, which will return a Series with the column names as the index and their corresponding data types as the values. This is useful for understanding the types of data in each column and for performing type-specific operations or conversions.    
print(df.values) # Get the underlying numpy array of the DataFrame, which will return a 2D array containing the values of the DataFrame without the index and column labels. This is useful for performing operations that require direct access to the data in a format suitable for numerical computations or machine learning algorithms.        
print(df.describe()) # Generate descriptive statistics for the DataFrame, which will provide summary information about the numerical columns (in this case, the 'Age' column) including count, mean, standard deviation, minimum, and maximum values. This is useful for quickly understanding the distribution and central tendencies of the data in the DataFrame.

print("Accessing specific rows and columns:")
print(df.loc[0:2]) 
print(df[(df['Age'] > 30) & (df['Age'] < 90)]) # Filter the DataFrame to include only rows where the 'Age' column is greater than 30, which will return a new DataFrame containing only the individuals who are older than 30 (Charlie in this case).
df.index = ['a', 'b', 'c'] # Set the index of the DataFrame to a new list of labels, which will replace the default integer index with the specified labels 'a', 'b', and 'c'. This allows for more meaningful row labels and can facilitate data selection and manipulation based on these custom indices.
print(df) # Display the DataFrame with the new index labels, which will show the updated
print(df.iloc[0]) # Access the first row of the DataFrame using the .iloc indexer, which will return a Series containing the data for the first individual (Alice) including their name, age, and city, now indexed by 'a' instead of 0.



# read the csv file
print("Reading data from a CSV file: ______________________________")
df_csv = pd.read_csv('Emp_info.csv') # Read a CSV file named 'data.csv' into a DataFrame, which will load the data from the file and create a structured DataFrame that can be used for data manipulation and analysis. Make sure to provide the correct path to the CSV file if it is not in the same directory as your script.
print(df_csv) # Display the contents of the DataFrame created from the CSV file, which will show the data that was loaded from 'Emp_info.csv' in a tabular format. This allows you to verify that the data has been read correctly and to inspect its structure and contents.
print("Data types of the columns in the CSV DataFrame:")
print(df_csv.dtypes)
print("First few rows of the CSV DataFrame:")
print(df_csv.head()) # Display the first few rows of the DataFrame created from the CSV file, which will return a new DataFrame containing the top 5 rows by default. This is useful for quickly inspecting the structure and contents of the DataFrame created from 'Emp_info.csv' without having to view the entire dataset.
print("Printing names and ages of the columns in the CSV DataFrame:")
print(df_csv[["Name", "Age"]]) # Access the 'Name' and 'Age' columns of the DataFrame created from the CSV file, which will return a DataFrame containing the names and ages of the individuals in the dataset loaded from 'Emp_info.csv'. This allows you to quickly view and analyze the names and ages of the employees in the CSV file.
# dropana example
print("Dropping rows with missing values in the CSV DataFrame:")
print(df_csv.dropna()) # Remove any rows with missing values from the DataFrame created from the CSV file, which will return a new DataFrame containing only the rows that have complete data without any null values. This is useful for cleaning the dataset and ensuring that subsequent analyses are performed on complete data.
# if columns have missing values
print("Dropping columns with missing values in the CSV DataFrame:")
print(df_csv.dropna(axis=1)) # Remove any columns with missing values from the DataFrame created from the CSV file, which will return a new DataFrame containing only the columns that have complete data without any null values. This is useful for cleaning the dataset and ensuring that subsequent analyses are performed on complete data, especially when certain columns are essential for analysis and cannot contain missing values.
#fillna example
print("Filling missing values in the CSV DataFrame with the mean age:")
print(df_csv.fillna(0)) # Fill any missing values in the DataFrame created from the CSV file with 0, which will return a new DataFrame where any null values are replaced with 0. This is useful for handling missing data when you want to ensure that all values are numeric and can be used in calculations or analyses without causing errors due to null values.

# fill forward example
print("Filling missing values in the CSV DataFrame using forward fill:")
print(df_csv.ffill()) # Fill any missing values in the DataFrame created from the CSV file using forward fill, which will return a new DataFrame where any null values are replaced with the last valid observation. This method propagates the last known value forward to fill in missing data, which can be useful for time series data or when you want to maintain the continuity of values in the dataset.
# fill backward example
print("Filling missing values in the CSV DataFrame using backward fill:")
print(df_csv.bfill()) # Fill any missing values in the DataFrame created from the CSV file using backward fill, which will return a new DataFrame where any null values are replaced with the next valid observation. This method propagates the next known value backward to fill in missing data, which can be useful for time series data or when you want to maintain the continuity of values in the dataset.

# example missed data with mean vlaue
print("Filling missing values in the 'Age' column of the CSV DataFrame with the mean age:")
print(df_csv['Age'].fillna(df_csv['Age'].mean())) # Fill any missing values in the age columns

#read cell valye
print(df_csv.loc[0,"Name"]) # Access the value in the first row and 'Name' column of the DataFrame created from the CSV file, which will return the name of the first individual in the dataset loaded from 'Emp_info.csv'. This allows you to quickly retrieve specific data points from the DataFrame based on row and column labels.


# add new column
print("Adding a new column 'Bonus'  'Salary' to the CSV DataFrame:")

df_csv["Bonus"] = df_csv["Salary"] * 0.1 # Add a new column 'Bonus' to the DataFrame created from the CSV file, which will calculate the bonus as 10% of the salary for each individual. This will return a new DataFrame with the additional 'Bonus' column containing the calculated bonus values based on the 'Salary' column.
print(df_csv)


# delete column
print("Deleting the 'Bonus' column from the CSV DataFrame:")
df_csv.drop("Bonus", axis=1, inplace=True) # Remove the 'Bonus' column from the DataFrame created from the CSV file, which will permanently delete the 'Bonus' column from the DataFrame. The axis=1 parameter specifies that a column is being dropped, and inplace=True ensures that the change is made directly to the original DataFrame rather than returning a new DataFrame.
print(df_csv) # Display the DataFrame after deleting the 'Bonus' column, which will


# merge two csv files
print("Merging two CSV DataFrames:")
df_csv2 = pd.read_csv('department.csv') # Read another CSV file named

merged_csvfile = pd.merge(df_csv, df_csv2) # Merge (this one is inner join merge) the two DataFrames created from the CSV files based on the 'Department' column, which will return a new DataFrame that combines the data from both DataFrames where the values in the 'Department' column match. This allows you to integrate information from both datasets based on a common key. print(merged_csvfile) # Display the merged DataFrame, which will show the combined data from both CSV files based on the matching 'Department' column. This allows you to verify that the merge was successful and to inspect the integrated dataset.   
print(merged_csvfile)

print("merged file mean salary by department:")
print(merged_csvfile.groupby('Department')['Salary'].mean()) # Group the merged DataFrame by the 'Department' column and calculate the mean salary for each department, which will return a Series with the department names as the index and their corresponding average salaries as the values. This allows you to analyze the average salary distribution across different departments in the merged dataset.
print(merged_csvfile.groupby('Department')['Salary'].max())
print(merged_csvfile.groupby('Department')['Salary'].min())
print(merged_csvfile.groupby('Department')['Salary'].sum())
print("merged file sorted by salary:")
print(merged_csvfile.sort_values('Salary', ascending=True))
print("merged file sorted by salary > 50000:    ")
print(merged_csvfile[merged_csvfile['Salary'] > 50000]) # Filter the merged DataFrame to include only rows where the 'Salary' column is greater than 50,000, which will return a new DataFrame containing only the individuals with salaries above that threshold. This allows you to analyze the higher earners in the merged dataset. 



# read the Excel file
print("Reading data from an Excel file: ______________________________")
#df_excel = pd.read_excel('Emp_info_.xlsx') # Read an Excel file named 'data.xlsx' into a DataFrame, which will load the data from the specified Excel file and create a structured DataFrame that can be used for data manipulation and analysis. Make sure to provide the correct path to the Excel file if it is not in the same directory as your script.  
