# imports
import pandas as pd

# 
data = pd.read_csv('dataset.csv')

# column selection
column1 = input("enter column name:")
filt1 = input("enter value:")
column2 = input("enter column name:")

if column1 in data.columns and column2 in data.columns:
    print(data[[column1, column2]])
else:
    print("not column")
