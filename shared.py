import pandas as pd

df = pd.read_csv('BRCA.csv')

df_only_female = df[df["Gender"] == "FEMALE"]


dfresult = df_only_female.dropna()

dfresult.to_csv('updatedData.csv')