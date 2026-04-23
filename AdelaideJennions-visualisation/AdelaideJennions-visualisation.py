import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

data = pd.read_excel('dataset.xlsx') # Reads the data set

# Is there a trend between loudness and energy?

def loudnessEnergyTrend(df):
    columns = data[['loudness', 'energy']] # selects the columns for loudness and energy

    sample_df = columns.dropna().sample(n=500, random_state=42) # reduces the dataset size by taking a random sample of 500 rows
    
    x = sample_df['loudness']
    y = sample_df['energy']

    #Scatter graph
    m, b = np.polyfit(x, y, 1) 
    plt.figure(figsize=(9, 6))
    plt.scatter(x, y, s=25, alpha=0.7)
    plt.plot(x, m*x + b, color='hotpink', linewidth=2)

    plt.title("Is there a trend between loudness and energy?", fontsize=14)
    plt.xlabel("Loudness", fontsize=12)
    plt.ylabel("Energy", fontsize=12)
    plt.grid(True)

    plt.tight_layout()
    plt.show()


    # Does the genre of a song affect its tempo?

def genreTempoQuery(df):
    columns = data[['track_genre', 'tempo']] # selects the columns for genre and tempo

    average_tempo = columns.groupby('track_genre')['tempo'].mean().sort_values() # calculates the average tempo for each genre
    
    print(average_tempo)

    plt.figure(figsize=(13,7))
    average_tempo.plot(kind='bar', color='hotpink')
    plt.title("Does the genre of a song affect its tempo?", fontsize=14)
    plt.xlabel("Genre", fontsize=12)
    plt.ylabel("Average Tempo", fontsize=12)

    plt.tight_layout()
    plt.show()

loudnessEnergyTrend(data)
genreTempoQuery(data)

   
