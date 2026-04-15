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
        avg1 = df[column1].mean() #calulates averge for column
        avg2 = df[column2].mean()

        print("\n====AVERAGE RESULTS====")
        print(f"Average of {column1}  {avg1:.2f}")
        print(f"Average of {column2}: {avg2:.2f}")
    except Exception as e:
        print("Error calculating the average:", e)

    # Query menu
    while True:

        print("===RESEARCH QUERIES MENU===")
        print("1. Most Popular Genre")
        print("2. Genre with Shortest/Longest Songs")
        print("3. Custom Query (Pick Two Columns)")
        print("4  Back to Main Menu")

        
        try:
            query_choice = int(input("Select query (1-4): "))
        except:
            print("Enter a number!")
            continue
            
        if query_choice == 1:
            print("\nQUERY 1: Most Popular Genre")

            genre_popularity = df.groupby("track_genre")["popularity"].mean() #calulates the avergae popularity for each genre

            print("\Average popularity by genre:")
            print(genre_popularity)

            top_genre = genre_popularity.idxmax() #finds the genre with the highest popularity 
            top_value = genre_popularity.max() 

            print("==========================================================")
            print(f"----- Most Popular Genre ------")
            print(f"The most popular genre is: {top_genre}")
            print(f"With the average of popularity being: {top_value: .2f}")
            print("==========================================================")
                
        elif query_choice == 2:
            print("\nQUERY 2: Genre with Shortest/longest songs")
            
            genre_length = df.groupby("track_genre")["duration_ms"].mean() #

            print("\nAvergae song length per genre:")
            print(genre_length)

            longest = genre_length.idxmax() #finds genre with the longest songs
            shortest = genre_length.idxmin() #finds genre wiht the shortest songs 

            print("================================================")
            print(f"genre with longest songs is: {longest}")
            print(f"genre with the shortest songs is: {shortest}")
            print("==================================================")

            
        elif query_choice == 3:
            print("\n======Custom Query:=============") 
            print("Available:", list(df.columns[5:])) 
            print("=================================")
            col1 = input("Column 1: ").strip() #input validation for column names 
            col2 = input("Column 2: ").strip()

            if column1 in df.columns and column2 in df.columns: 

                corr = df[column1].corr(df[column2])
                print("\n----------------TREND RESULT-------------------------------")
                print(f"Correlation between {column1} and {column2}: {corr: .3f}") #calulates the correlation 
            
                if corr > 0.5:
                     print("- Positive Trend ")
                elif corr < -0.5:
                     print("- Negative Trend")
                else: 
                     print("- Weak Trend")

                avg1 = df[column1].mean()
                avg2 = df[column2].mean()
               
                print()
                print("------AVERAGE RESULTS--------")
                print(f"Average of {column1}  {avg1:.2f}")
                print(f"Average of {column2}: {avg2:.2f}")
                print("-----------------------------")
          
            else:
                print("Invalid columns")
            
        elif query_choice == 4:
            print("Returning to main menu...")
            return
            
        else:
            print("Choose 1-4")

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
