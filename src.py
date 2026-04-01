import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('dataset.csv') # Reads the data set

#-----------------------FUNCTIONS-----------------------
#Trend-Based Function ---
def trendBasedEnquiry(df):
    filtered_columns = df.columns[5:] #removes non-useful column options like track_name etc.
    
    print("\nAvailable columns:")
    print(list(filtered_columns))

    # Input validation loop
    while True:
        print("\nEnter first column name: ", end="", flush=True)
        column1 = input()
        print("Enter second column name: ", end="", flush=True)
        column2 = input()

        if column1 in df.columns and column2 in df.columns:
            break
        else:
            print("Invalid column name(s). Please try again.")

    # Show selected columns
    print(df[[column1, column2]])

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df[column1], df[column2])

    x = df[column1]
    y = df[column2]
    m, b = np.polyfit(x, y, 1)
    ax.plot(x, m*x + b, color='red', linewidth=3)

    ax.set_title(f"{column1} vs {column2}")
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    ax.grid(True)

    plt.show()


#Average-Based Function ---


#-----------------------MAIN PROGRAM-----------------------

#Opening Menu -----------------------------

while True:
    print("\n--- Main Menu ---")
    print("1. Trend-Based Enquiry")
    print("2. Average-Based Enquiry")
    print("3. Exit")

    try:
        initialMenuSelection = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input — please enter a number.") #input validation
        continue

    if initialMenuSelection == 1:
        print("--- Trend-Based Enquiry ---")
        try:
            trendBasedEnquiry(data) #calls trend-based function (above)
        except Exception as e:
            print("ERROR:", e)

    elif initialMenuSelection == 2:
        print("--- Average-Based Enquiry ---")
        # call average function here

    elif initialMenuSelection == 3:
        print("Thank You For Using The System")
        break

    else:
        print("Invalid choice — please enter 1, 2, or 3.")