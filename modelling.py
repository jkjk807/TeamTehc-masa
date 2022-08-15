from random import randint
import pandas as pd
import joblib
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RepeatedStratifiedKFold

#Importing dataset and cleaning data.
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

#Decision tree with output claim.
dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)
predict = dtc.predict(X_test)
accuracy = accuracy_score(y_test, predict)
print(accuracy)

#Logistic regression
lr = LogisticRegression()
lr.fit(X_train, y_train)
predict = lr.predict(X_test)
accuracy = accuracy_score(y_test, predict)
print(accuracy)

#SGD
sgd = SGDClassifier()
sgd.fit(X_train, y_train)
predict = sgd.predict(X_test)
accuracy = accuracy_score(y_test, predict)
print(accuracy)

#Random forest
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
predict = rf.predict(X_test)
accuracy = accuracy_score(y_test, predict)
cv = cross_val_score(rf, X_train, y_train, cv=5)
score = rf.score(X_test, y_test)
print(accuracy, cv.mean(), score)

#SVC
svc = SVC(probability=True, C = 1, kernel="linear")
svc.fit(X_train, y_train)
predict = svc.predict(X_test)
accuracy = accuracy_score(y_test, predict)
cv = cross_val_score(rf, X_train, y_train, cv=5)
score = svc.score(X_test, y_test)
print(accuracy, cv.mean(), score)

#Tuning using randomized search
param = {
    "max_depth": [3, None],
    "max_features": [randint(1, 9)],
    "min_samples_leaf": [randint(1, 9)],
    "criterion": ["gini", "entropy"]
}

dtc = DecisionTreeClassifier()
dtc_cv = RandomizedSearchCV(dtc, param, cv=5)
dtc_cv.fit(X_train, y_train)
print(dtc_cv.best_params_, dtc_cv.best_score_)

#Tuning using grid
param = {
    "n_estimators": [200, 500],
    "max_depth": [4,5,6,7,8],
    "criterion": ["gini", "entropy"]
}

rf = RandomForestClassifier()
rf_cv = GridSearchCV(estimator=rf, param_grid=param, cv=5)
rf_cv.fit(X_train, y_train)
print(rf_cv.best_params_, rf_cv.best_score_)