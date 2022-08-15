from random import randint
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV

#Importing dataset, cleaning data and preparing data.
df = pd.read_excel("C:\\Users\\notth\\Documents\\MASA Hackathon\Documentation & Materials\\TravelDataset.xlsx")
df = df.drop(df[(df["Net Sales"] < 0) | (df["Duration"] < 0)].index)
df = df.drop(columns=["Gender", "Net Sales", "Commision (in value)"])

X = df.drop(columns=["Claim"])
y = df["Claim"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

enc = OneHotEncoder(handle_unknown="ignore")
X_train = enc.fit_transform(X_train)
X_test = enc.transform(X_test)

le = LabelEncoder()
y_train = le.fit_transform(y_train)
y_test = le.transform(y_test)

#Decision tree.
dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)
predict = dtc.predict(X_test)
accuracy = accuracy_score(y_test, predict)
print(accuracy)

#Tuning using randomized search.
param_rs = {
    "max_depth": [3, None],
    "max_features": [randint(1, 9)],
    "min_samples_leaf": [randint(1, 9)],
    "criterion": ["gini", "entropy"]
}
dtc_rs = RandomizedSearchCV(dtc, param_rs, cv=5)
dtc_rs.fit(X_train, y_train)
print(dtc_rs.best_params_, dtc_rs.best_score_)

#Tuning using grid search.
param_gs = {
    "ccp_alpha": [0.1, 0.01, 0.001],
    "max_depth": [5, 6, 7, 8, 9],
    "criterion": ["gini", "entropy"]
}
dtc_gs = GridSearchCV(estimator=dtc, param_grid=param_gs, cv=5, verbose=True)
dtc_gs.fit(X_train, y_train)
print(dtc_gs.best_params_, dtc_gs.best_score_)