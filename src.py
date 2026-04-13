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
        print("\nPlease enter the first column name: ", end="", flush=True)
        column1 = input()
        print("Please enter the second column name: ", end="", flush=True)
        column2 = input()

        if column1 in df.columns and column2 in df.columns:
            break
        else:
            print("Invalid column name(s). Please try again.")

    # Show selected columns
    print(df[[column1, column2]])

    # Reduce dataset size - random sample
    sample_df = df[[column1, column2]].dropna().sample(n=500, random_state=42)
                              
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(8, 5))

    ax.scatter(sample_df[column1], sample_df[column2], s=25, alpha=0.75)

    x = sample_df[column1]
    y = sample_df[column2]

    m, b = np.polyfit(x, y, 1)
    
    ax.plot(x, m*x + b, color='red', linewidth=2)
    
    ax.set_title(f"{column1} vs {column2}", fontsize=14)
    ax.set_xlabel(column1, fontsize=12)
    ax.set_ylabel(column2, fontsize=12)
    ax.grid(True)

    plt.tight_layout()
    plt.show()


#Average-Based Function ---
def averageBasedEnquiry(df):
    filtered_columns = df.columns[5:] #removes the columns that aren't needed, e.g. track_name etc.


    print("\n--Average-Based Enquiry--")

    print("\nAvailable Columns")
    print(list(filtered_columns)) 
    while True:
        print("\nPlease enter the first column name: ", end="", flush=True)
        column1 = input().strip
        print("\nPlease enter the second column name:", end="", flush=True)
        column2 = input().strip

        if column1 in df.columns and column2 in df.columns:
            break
        else:
            print("Invalid column name(s). Please try again.")

    #Averages calculations 
    print(f"\nYou have selected: {column1} and {column2}")

       try:
        avg1 = df[column1].mean()
        avg2 = df[column2].mean()
        
        print("\n-- Average Results --")  
        print(f"Average of {column1}: {avg1:.2f}")
        print(f"Average of {column2}: {avg2:.2f}")

    except Exception as e:
    print("Error calclulating the average:", e)

    #add in additional functionality (create another enquiry) here
while True:
    print("\nWould you like to make another average enquiry? (yes/no): ", end="", flush=True)
    again = input().strip().lower()

    if again == "yes":
        averageBasedEnquiry(df) 
        return
    elif again == "no":
        print("Returning to the main menu...")
        return
        break
    else:
        print("Invalid input – please type 'yes' or 'no:'")


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
        try: 
            averageBasedEnquiry(data)
        except Exception as e: 
            print("ERROR:", e)

    elif initialMenuSelection == 3:
        print("Thank You For Using The System")
        break

    else:
        print("Invalid choice — please enter 1, 2, or 3.")
