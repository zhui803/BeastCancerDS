import pandas as pd

df = pd.read_csv('BRCA.csv')

df_only_female = df[df["Gender"] == "FEMALE"]


print(df_only_female.to_string())

#print(df.to_string()) 