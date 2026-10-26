import pandas as pd

df = pd.read_csv("data/raw/train-selected-columns.csv")

print(df.shape)
print("SalePrice" in df.columns)
print(df.columns)
