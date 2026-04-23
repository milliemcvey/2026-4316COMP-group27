import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel("dataset.xlsx") # Reads the dataset from excel

# How does the liveness affect the popularity?
# Columns: Liveness, Popularity

def livenessPopularityQuery(data):
    columns = data[['liveness', 'popularity']]

    liveness = columns.groupby('liveness')['popularity'].mean().sort_values() # Takes sample from each column

    print(liveness)

    plt.figure(figsize=(11, 8))
    liveness.plot(kind='bar', color='crimson')
    plt.title("How does the liveness affect the popularity", fontsize=15)
    plt.xlabel("Liveness", fontsize=14)
    plt.ylabel("Popularity", fontsize=14)
    plt.tight_layout()
    plt.show()

# Does the acousticness affect the danceability?
# Columns: Acousticness, Danceability

def acousticnessDanceabilityTrendQuery(data): # Selects which columns will be used for the query
    columns = data[['acousticness', 'danceability']]

    sample = columns.dropna().sample(n=500, random_state=42) # Samples columns from the dataset

    x = sample['acousticness'] # Grabs the two columns and plots them on the chosen axis
    y = sample['danceability']

    plt.figure(figsize=(11, 8)) # Creates the scatter graph
    plt.scatter(x, y, s=25, alpha=0.75)

    m, b = np.polyfit(x, y, 1) # Correlation line
    plt.plot(x, m*x + b, color='turquoise', linewidth=2)

    plt.title("Does the acousticness affect the danceability?", fontsize=15)
    plt.xlabel("Acousticness", fontsize=14)
    plt.ylabel("Danceability", fontsize=14)
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Calls both functions
livenessPopularityQuery(data)
acousticnessDanceabilityTrendQuery(data)
