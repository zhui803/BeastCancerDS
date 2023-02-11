import pandas as pd

df = pd.read_csv('BRCA.csv')
dfU = pd.read_csv('updatedData.csv')

df_only_female = df[df["Gender"] == "FEMALE"]
dfU_only_female = dfU[dfU["Gender"] == "FEMALE"]


print(dfU_only_female.to_string())

df.to_csv('DF_Only_Female.csv')

#print(df.to_string()) 