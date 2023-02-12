import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('updatedData.csv')

protein1 = df["Protein1"].tolist
protein2 = df["Protein2"].tolist
protein3 = df["Protein3"].tolist
protein4 = df["Protein4"].tolist
tumourStages = df["Tumour_Stage"]

#convert tumour stages to ints

tumourStagesInt = []

for i in range(len(tumourStages)):
    if (tumourStages[i]) == "I":
        tumourStagesInt.append(1)
    elif (tumourStages[i]) == "II":
        tumourStagesInt.append(2)
    else:
        tumourStagesInt.append(3)

plt.scatter([1,2,3,4],[1.4,2.5,3.2,4.5])
plt.show()

print(tumourStagesInt)