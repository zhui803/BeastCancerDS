import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

import numpy as np

df = pd.read_csv('BRCA.csv')
dfU = pd.read_csv('updatedData.csv')

df_only_female = df[df["Gender"] == "FEMALE"]
dfU_only_female = dfU[dfU["Gender"] == "FEMALE"]

dfU_Proteins = dfU[["Protein1", "Protein2", "Protein3", "Protein4"]]

stage_map = {"I" : 1, "II" : 2, "III" : 3}

dfU['Stage'] = df['Tumour_Stage'].map(stage_map)

markers = ['o', 'x', 'd', 'o']
colors = ['purple', 'cyan', 'green', 'yellow']
legend_handles = []

for i, col_name in enumerate(dfU_Proteins.columns): 
    sns.scatterplot(data=dfU_Proteins, x=dfU['Stage'], y=dfU_Proteins.index,
                    marker=markers[i], color=colors[i], s=100) # s = marker size
    legend_handles.append(mlines.Line2D([], [], color=colors[i], marker=markers[i],
                                        linestyle='None', markersize=8, label=col_name))

plt.scatter(dfU["Stage"], dfU["Protein1"], linestyle="None")
plt.show()

#print(dfU_only_female.to_string())
sns.scatterplot(data = dfU, x = "Stage", y = "Protein1")
plt.show()


#print(df.to_string()) 