from audioop import cross
import pandas as pd
import joblib
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC


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