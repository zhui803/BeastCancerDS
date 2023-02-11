import pandas as pd

df = pd.read_csv('BRCA.csv')

df_only_female = df[df["Gender"] == "FEMALE"]