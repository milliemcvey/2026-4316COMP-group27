import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_excel("dataset.xlsx")
data.columns = data.columns.str.strip().str.lower()



def durationDanceabilityEnquiry(data):
    columns = data[['duration_ms', 'danceability']].dropna()

    
    x = columns['duration_ms'] / 1000
    y = columns['danceability']

    plt.figure(figsize=(8, 5))

   
    plt.scatter(x, y, color='lightcoral', alpha=0.5)

    
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m*x + b, color='darkred')

    plt.title("Duration vs Danceability")
    plt.xlabel("Duration (seconds)")
    plt.ylabel("Danceability")

    plt.grid(True)
    plt.tight_layout()
    plt.show()



def explicitEnergyEnquiry(data):
    columns = data[['explicit', 'energy']].dropna()

    avg_energy = columns.groupby('explicit')['energy'].mean()

    plt.figure(figsize=(6, 5))

    avg_energy.plot(kind='bar', color=['mistyrose', 'darkred'])

    plt.xticks([0, 1], ['Non-Explicit', 'Explicit'], rotation=0)

    plt.title("Average Energy: Explicit vs Non-Explicit")
    plt.ylabel("Energy")

    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()



def main():
    print("Select an option:")
    print("1 - Duration vs Danceability")
    print("2 - Explicit vs Energy")
    print("3 - Show BOTH graphs")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        durationDanceabilityEnquiry(data)
    elif choice == '2':
        explicitEnergyEnquiry(data)
    elif choice == '3':
        durationDanceabilityEnquiry(data)
        explicitEnergyEnquiry(data)
    else:
        print("Invalid choice. Please run again.")


main()
