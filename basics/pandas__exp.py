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


