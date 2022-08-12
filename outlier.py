import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from IPython.display import display

#Read excel file.
df = pd.read_excel("C:\\Users\\notth\\Documents\\MASA Hackathon\\Documentation & Materials\\TravelDataset.xlsx")
df_cleaned= df.drop(df[(df["Net Sales"] < 0) | (df["Duration"] < 0)].index)

#To observe outliers with boxplot
column = df_cleaned["Age"]
sns.boxplot(y=column)
plt.show()

#To observe outliers with interquartile range
#Write to excel for better viewing of full table
tmp = pd.DataFrame()
file_name = "AgeData.xlsx"
first_quartile = np.percentile(df_cleaned["Age"], 25, method="midpoint")
third_quartile = np.percentile(df_cleaned["Age"], 75, method="midpoint")
iqr = third_quartile - first_quartile

upper_bound = np.where(df_cleaned["Age"] >= third_quartile + 1.5 * iqr)
lower_bound = np.where(df_cleaned["Age"] <= first_quartile - 1.5 * iqr)
i = 0
while i < len(upper_bound):
    tmp = pd.concat([tmp, df_cleaned.iloc[upper_bound[i]]])
    tmp = pd.concat([tmp, df_cleaned.iloc[lower_bound[i]]])
    i += 1

display(tmp)
tmp.to_excel(file_name)