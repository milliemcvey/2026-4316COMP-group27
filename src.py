import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('dataset.csv') # Reads the data set

#-----------------------FUNCTIONS-----------------------
#Trend-Based Function
def trendBasedEnquiry(df):
    print("\nAvailable columns:")
    print(list(df.columns))

    # Input validation loop
    while True:
        column1 = input("\nEnter first column name: ")
        column2 = input("Enter second column name: ")

        if column1 in df.columns and column2 in df.columns:
            break
        else:
            print("Invalid column name(s). Please try again.")

    # Show selected columns
    print(df[[column1, column2]])

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df[column1], df[column2])

    ax.set_title(f"{column1} vs {column2}")
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    ax.grid(True)

    plt.show()


#Average-Based Function

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
        # call your trend function here

    elif initialMenuSelection == 2:
        print("--- Average-Based Enquiry ---")
        # call your average function here

    elif initialMenuSelection == 3:
        print("Thank You For Using The System")
        break

    else:
        print("Invalid choice — please enter 1, 2, or 3.")