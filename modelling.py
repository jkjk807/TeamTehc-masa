import pandas as pd
import joblib
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#Importing dataset and cleaning data.
df = pd.read_excel("C:\\Users\\notth\\Documents\\MASA Hackathon\Documentation & Materials\\TravelDataset.xlsx")
df = df.drop(df[(df["Net Sales"] < 0) | (df["Duration"] < 0)].index)
df = df.drop(columns=["Gender", "Net Sales", "Commision (in value)"])

df["Claim"].replace(["Yes", "No"],
                    [1, 0], inplace=True)

X = df.drop(columns=["Claim"])
y = df["Claim"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

enc = OneHotEncoder(handle_unknown="ignore")
X_train = enc.fit_transform(X_train)
X_test = enc.transform(X_test)

le = LabelEncoder()
y_train = le.fit_transform(y_train)
y_test = le.transform(y_test)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
predict = model.predict(X_test)
accuracy = accuracy_score(y_test, predict)
print(accuracy)