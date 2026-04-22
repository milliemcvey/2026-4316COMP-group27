import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel("dataset.xlsx") # Reads the data set

# Does the tempo of a song affect the popularity?

def tempoPopularityEnquiry(data):
    columns = data[['tempo' , 'popularity']]

    # Sample from the columns
    sample = columns.dropna().sample(n=500, random_state=42)

    x = sample['tempo']
    y = sample['popularity']
                              
    # Create scatter plot
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, s=25, alpha=0.75)

    # Correlation line
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m*x + b, color='red', linewidth=2)
    
    plt.title("Does the tempo of a song affect the popularity?" , fontsize=14)
    plt.xlabel("Tempo in bpm", fontsize=12)
    plt.ylabel("Popularity", fontsize=12)
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Is there a genre with the longest/shortest songs?

def genreSongLength(data):
    columns2 = data[['track_genre' , 'duration_ms']]

    columns2['duration_s'] = columns2['duration_ms'] / 1000 # convert duration to seconds

    avg_lengths = columns2.groupby('track_genre')['duration_s'].mean().sort_values()
    
    # Prints average lengths for each genre
    print(avg_lengths)

    # Create bar chart
    plt.figure(figsize=(12, 6))
    avg_lengths.plot(kind='bar', color='red')
    plt.title("Is there a genre with the longest/shortest songs?", fontsize=14)
    plt.xlabel("Genre", fontsize=12)
    plt.ylabel("Average Length in seconds", fontsize=12)
   
    plt.tight_layout()
    plt.show()

tempoPopularityEnquiry(data)
genreSongLength(data)