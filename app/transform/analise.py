import pandas as pd

df = pd.read_csv("data/final_data.csv", sep=";")
print(df.columns)