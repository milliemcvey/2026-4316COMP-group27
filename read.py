# Is a higher energy track more  (e.g)?

import pandas as pd

data = pd.read_csv('dataset.csv')

filtered = data[(data["popularity"] > 80) & (data["energy"] > 0.8)]

new_data = filtered[["track_name", "popularity", "energy"]]

print(new_data)