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
    print("\n--Average-Based Enquiry--")
    print("\nAvailable Columns:")
    print(list(filtered_columns))
    
    while True:
        print("\nPlease enter the first column name: ", end="", flush=True)
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
        avg1 = df[column1].mean()
        avg2 = df[column2].mean()
        print("\n-- Average Results --")
        print(f"Average of {column1}: {avg1:.2f}")
        print(f"Average of {column2}: {avg2:.2f}")
    except Exception as e:
        print("Error calculating the average:", e)

    # Query menu
    while True:
        print("\n" + "="*50)
        print("RESEARCH QUERIES MENU")
        print("1. Does explicit content affect popularity?")
        print("2. Does song length affect popularity?")
        print("3. Custom average enquiry")
        print("4. Back to main menu")
        print("="*50)
        
        try:
            query_choice = int(input("Select query (1-4): "))
        except:
            print("Enter a number!")
            continue
            
        if query_choice == 1:
            print("\nQUERY 1: Explicit vs Popularity")
            try:
                explicit_pop = df.groupby('explicit')['popularity'].mean()
                print(f"Non-explicit avg popularity: {explicit_pop[0]:.2f}")
                print(f"Explicit avg popularity: {explicit_pop[1]:.2f}")
                print(f"INSIGHT: {'Explicit songs are MORE popular' if explicit_pop[1]>explicit_pop[0] else 'Explicit songs are LESS popular'}")
            except:
                print("Columns 'explicit' or 'popularity' not found")
                
        elif query_choice == 2:
            print("\nQUERY 2: Duration vs Popularity")
            try:
                df['duration_min'] = df['duration_ms'] / 60000
                short_songs = df[df['duration_min'] < df['duration_min'].median()]
                long_songs = df[df['duration_min'] >= df['duration_min'].median()]
                print(f"Short songs avg: {short_songs['popularity'].mean():.2f}")
                print(f"Long songs avg: {long_songs['popularity'].mean():.2f}")
                print(f"INSIGHT: {'Longer songs are MORE popular' if long_songs['popularity'].mean() > short_songs['popularity'].mean() else 'Shorter songs are MORE popular'}")
            except:
                print("Columns 'duration_ms' or 'popularity' not found")
                
        elif query_choice == 3:
            print("\nCustom enquiry:")
            print("Available:", list(df.columns[5:]))
            col1 = input("Column 1: ").strip()
            col2 = input("Column 2: ").strip()
            if col1 in df.columns and col2 in df.columns:
                print(f"{col1}: {df[col1].mean():.3f}")
                print(f"{col2}: {df[col2].mean():.3f}")
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
