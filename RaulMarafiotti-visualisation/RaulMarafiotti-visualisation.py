import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel("code/dataset.xlsx")
data.columns = data.columns.str.strip().str.lower()


# checks if energy affects danceability
def energyDanceabilityEnquiry(data):
    columns = data[['energy', 'danceability']].dropna()

    sample = columns.sample(n=500, random_state=42)

    x = sample['energy']
    y = sample['danceability']

    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, alpha=0.6)

    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m*x + b, linewidth=2)

    plt.title("Energy vs Danceability", fontsize=14)
    plt.xlabel("Energy", fontsize=12)
    plt.ylabel("Danceability", fontsize=12)
    plt.grid(True, linestyle=':')

    plt.tight_layout()
    plt.show()


# checks if song length affects popularity
def lengthPopularityEnquiry(data):
    columns = data[['duration_ms', 'popularity']].dropna()

    columns['duration_s'] = columns['duration_ms'] / 1000

    sample = columns.sample(n=500, random_state=42)

    x = sample['duration_s']
    y = sample['popularity']

    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, alpha=0.6)

    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m*x + b, linewidth=2)

    plt.title("Song Length vs Popularity", fontsize=14)
    plt.xlabel("Length (seconds)", fontsize=12)
    plt.ylabel("Popularity", fontsize=12)
    plt.grid(True, linestyle='--')

    plt.tight_layout()
    plt.show()


energyDanceabilityEnquiry(data)
lengthPopularityEnquiry(data)
