import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter 
import seaborn as sns
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder,  LabelEncoder
from sklearn.model_selection import train_test_split


from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier

df = pd.read_csv("dataset/travel_insurance_data_set.csv")

def bar_plot(dataframe,variable, colors):
    """
        input: variable ex: "Sex"
        output: bar plot & value count
    """
    # get feature
    var = dataframe[variable]
    
    # count number of categorical variable(value/sample)
    varValue = var.value_counts()
    
    # visualize
    plt.figure(figsize = (9,3))
    plt.bar(varValue.index, varValue,color=colors[4])
    plt.xticks(varValue.index, varValue.index.values)
    plt.ylabel("Frequency")
    plt.title(variable)
    plt.show()

# colors = sns.color_palette('pastel')
# category1 = ["Agency" , "Agency Type" , "Product Name"]
# for c in category1:
#     bar_plot(df, c,colors)

tmp = df[["Duration" , "Gender", "Net Sales", "Commision (in value)"]]
print(tmp.info())

corr = tmp.corr(method ='pearson')
print(corr)

import seaborn as sns
sns.heatmap(corr, 
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values)




# print(df.describe())
# print(df.info())