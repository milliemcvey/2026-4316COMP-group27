import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel("dataset.xlsx") # To read the data set

# Does the key of a song affect the popularity?
# Key and Popularity 

def keyPopularityQuery(data):
    columns = data[['key', 'popularity']]

    # The average popularity for each key
    averagePopularity = columns.groupby('key')['popularity'].mean().sort_values()

    # Printing the average popularity values
    print(averagePopularity)

    # Creates a bar chart
    plt.figure(figsize=(12, 6))
    averagePopularity.plot(kind='bar', color='green')

    plt.title("Does the key of a song affect the popularity?", fontsize=14)
    plt.xlabel("Key", fontsize=12)
    plt.ylabel("Average Popularity", fontsize=12)

    plt.tight_layout()
    plt.show()


# Are explicit songs louder than others?
# Explicit and Loudness

def explicitLoudnessQuery(data):
    columns2 = data[['explicit', 'loudness']]
    
    # The average loudness 
    averageLoudness = columns2.groupby('explicit')['loudness'].mean().sort_values()
    averageLoudness.index = ['Non-Explicit', 'Explicit']
    print(averageLoudness)

    # Creating the bar chart
    plt.figure(figsize=(12,6))
    averageLoudness.plot(kind='bar', color='green')

    plt.title("Are explicit songs louder than others?", fontsize=14)
    plt.xlabel("Song Type", fontsize=12)
    plt.ylabel("Average Loudness", fontsize=12)

    plt.tight_layout()
    plt.show()

keyPopularityQuery(data)
explicitLoudnessQuery(data)