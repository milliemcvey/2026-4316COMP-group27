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

# average-based function

def averageBasedEnquiry(df):
    filtered_columns = df.columns[5:] 
    print("\nAverage-Based Enquiry")
    print("\nAvailable Columns:")
    print(list(filtered_columns)) #displays columns for the user to choose from 
    
    while True:
        print("\nPlease enter the first column name: ", end="", flush=True) #input validation for column names 
        column1 = input().strip()
        print("Please enter the second column name: ", end="", flush=True)
        column2 = input().strip()

        if column1 in df.columns and column2 in df.columns:
            break
        else:
            print("Invalid column name(s). Please try again.")

    print(f"\nYou have selected: {column1} and {column2}")

    # average calculations
    try:
        clean_df = df[[column1,column2]].dropna()

        if not pd.api.types.is_numeric_dtype(clean_df[column1]) or not pd.api.types.is_numeric_dtype(clean_df[column2]):
           print("Error: Both selected columns must be numeric.")
        return
        
        avg1 = df[column1].mean() #calulates averge for column
        avg2 = df[column2].mean()

        median1 = clean_df[column1].median() # calculate median
        median2 = clean_df[column2].median()

        print("\n====AVERAGE RESULTS====")
        print(f"Average of {column1}  {avg1:.2f}, median={median1:.2f}")
        print(f"Average of {column2}: {avg2:.2f}, median={median2:.2f}")")
       
        # Create bar chart 
        fig, ax = plt.subplots(figsize=(8, 5))

        labels = [column1, column2]
        values = [avg1, avg2]

        ax.bar(labels, values)

        ax.set_title(f"Average Comparison: {column1} vs {column2}", fontsize=14)
        ax.set_xlabel(f"{column1} vs {column2}", fontsize=12)
        ax.set_ylabel("Average Value", fontsize=12)
        ax.grid(True)

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print("Error calculating the average:", e)

    # Query menu
def customQuery(df):
    filtered_columns = df.columns[5:]

    print("====CUSTOM QUERY====")
    print("Available Columns:")
    print(list(filtered_columns))
    print("*****ONLY ENTER ANY TEXT BASED COLUMNS IN COLUMN 1*****")

    while True:
        print("\nPlease enter the first column name: ", end="", flush=True)
        column1 = input()
        print("\nPlease enter the second column name: ", end="", flush=True)
        column2 = input()

        if column1 not in df.columns or column2 not in df.columns:
            print("Invalid column name(s). Please try again.")
            continue
        
        is_num1 = pd.api.types.is_numeric_dtype(df[column1])
        is_num2 = pd.api.types.is_numeric_dtype(df[column2])

        # ---- TEXT + NUMERIC ----
        if not is_num1 and is_num2:
            grouped_summary = df.groupby(column1)[column2].mean()
             
            print("Average values by category:")
            print(grouped_summary)

            most = grouped_summary.idxmax()
            least = grouped_summary.idxmin()
            top_value = grouped_summary.max()

            print("==============")
            print("Grouped Summary:")
            print(f"Highest Rated: {most}")
            print(f"Lowest Rated: {least}")
            print(f"With the average being: {top_value:.2f}")
            print("==============")

            break  # ✅ return to main menu

        # ---- NUMERIC + NUMERIC ----
        elif is_num1 and is_num2:
            x = df[column1]
            y = df[column2]

            corr = x.corr(y)
            avg1 = x.mean()
            avg2 = y.mean()
            
            print("========================================")
            print("        NUMERIC CORRELATION       ")
            print(f"\nCorrelation between {column1} and {column2}: {corr:.2f}")

            if corr > 0.5:
                print("STRONG POSITIVE CORRELATION")
            elif corr < -0.5:
                print("STRONG NEGATIVE CORRELATION")
            elif corr > 0.2:
                print("MODERATE POSITIVE CORRELATION")
            elif corr < -0.2:
                print("MODERATE NEGATIVE CORRELATION")
            else:
                print("WEAK OR NO CORRELATION")
            
            print("======================================")
            print("          AVERAGE RESULTS         ")
            print(f"\nAverage of {column1}: {avg1:.2f}")
            print(f"Average of {column2}: {avg2:.2f}")
            print("======================================")

            break 

        else:
            print("Unsupported column types. Try again.")


#-----------------------MAIN PROGRAM-----------------------

#Opening Menu -----------------------------

while True:
    print("\n--- Main Menu ---")
    print("1. Trend-Based Enquiry")
    print("2. Average-Based Enquiry")
    print("3. Create a Custom Query")
    print("4. Exit")

    try:
        initialMenuSelection = int(input("Please enter your choice: "))
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
        print("--- Create a Custom Query ---")
        try:
            customQuery(data) #calls query menu function (above)
        except Exception as e:
            print("Error:", e)

    elif initialMenuSelection == 4:
        print("Thank You For Using The System!")
        break

    else:
        print("Invalid choice — please enter 1, 2, 3, or 4.")
