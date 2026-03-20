#filter out the user input columns so its
#more precise and graph more readable

#make graphs more suited to the columns

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('dataset.csv')
#print column names
print("Columns:", list(data.columns))


column1 = input("enter column name:")
column2 = input("enter column name:")

#shows selected columns
if column1 in data.columns and column2 in data.columns:
    print(data[[column1, column2]])

    #matplotlib
    fig, ax = plt.subplots()  #figure and Axes

    ax.plot(data[column1], data[column2])  #y and x

    ax.set_title(f"{column1} vs {column2}")  #titles
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)

    plt.show()

else:
    print("not column")

