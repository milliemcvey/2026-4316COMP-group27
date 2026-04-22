import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel("dataset.xlsx") # Reads data from excel

# Investigation: Is there a "most popular genre"?
# Columns: Genre & Popularity

def genrePopularityQuery(data):
    columns = data[['track_genre' , 'popularity']]
    
    #Take a sample portion of each columns
    averageLengths = columns.groupby('track_genre')['popularity'].mean().sort_values()
    
    #Prints average popularity of each genre
    print(averageLengths)
    
    plt.figure(figsize=(12, 6))
    averageLengths.plot(kind='bar', color='red')
    plt.title("Is there a 'most popular genre'?")
    plt.xlabel("Genre", fontsize =12)
    plt.ylabel("Average Popularity", fontsize=12)
    plt.tight_layout()
    plt.show()
    
# Investigation: Does the key of a song affect the energy?
# Columns: Key & Energy

def keyEnergyQuery(data):
    columns2 = data[['key', 'energy']]
    
    #Sample from dataset
    sample = columns2.dropna().sample(n=1000, random_state=62)

    x = sample['key']
    y = sample['energy']
    
    #Creating scatter graph
    plt.figure(figsize=(12,6))
    plt.scatter( x, y, s=25, alpha=0.75)
    
    #Correlation line
    m, b = np.polyfit( x, y, 1)
    plt.plot(x, m*x + b, color='green', linewidth=2)
    
    plt.title("Does the key affect the energy?", fontsize=12)
    plt.xlabel("Key", fontsize=12)
    plt.ylabel("Energy Rating", fontsize=12)
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()
    
# Calling both functions:
genrePopularityQuery(data)
keyEnergyQuery(data)