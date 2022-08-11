import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from IPython.display import display

#To observe outliers with boxplot
def outlier_bp(df, colname):
    column = df[colname]
    sns.boxplot(y=column)
    plt.show()

#To observe outliers with interquartile range
def outlier_iqr(df, colname):
    tmp = pd.DataFrame()
    first_quartile = np.percentile(df[colname], 25, method="midpoint")
    third_quartile = np.percentile(df[colname], 75, method="midpoint")
    iqr = third_quartile - first_quartile

    upper_bound = np.where(df[colname] >= third_quartile + 1.5 * iqr)
    lower_bound = np.where(df[colname] <= first_quartile - 1.5 * iqr)
    i = 0
    while i < len(upper_bound):
        tmp = pd.concat([tmp, df.loc[upper_bound[i]]])
        tmp = pd.concat([tmp, df.loc[lower_bound[i]]])
        i += 1
    display(tmp)

#Read excel file.
df = pd.read_excel("C:\\Users\\notth\\Documents\\MASA Hackathon\\Documentation & Materials\\TravelDataset.xlsx")

#Looking for outliers of age using boxplot and interquartile range.
outlier_bp(df, "Age")
outlier_iqr(df, "Age")

#Looking for outliers of duration.
outlier_bp(df, "Duration")
outlier_iqr(df, "Duration")

#Looking for outliers of net sales.
outlier_bp(df, "Net Sales")
outlier_iqr(df, "Net Sales")

#Looking for outliers of commission.
outlier_bp(df, "Commision (in value)")
outlier_iqr(df, "Commision (in value)")