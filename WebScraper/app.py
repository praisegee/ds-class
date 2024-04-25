import json

import pandas as pd

with open("books.json") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# print(df.head())

df.to_csv("data.csv")
