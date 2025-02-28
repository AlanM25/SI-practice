import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler # necessary to reduce biases of large numbers
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
import numpy as np


dataset = pd.read_csv("resources/strange_flowers.txt",
                      header=None,
                      names=["red", "green", "blue", "size", "label"],
                      sep=" ")

data = dataset.drop('label', axis=1)
labels = dataset.label

X_train, X_test, y_train, y_test = train_test_split(data, labels, random_state=0, test_size=0.2)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train) #  transform
X_test = scaler.transform(X_test) #  transform

k = int(len(X_train) ** 0.5)
# Define the model
classifier = KNeighborsClassifier(n_neighbors=k,
                                  metric="minkowski",
                                  p=2,    # Euclidian
                                 )
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print(y_pred)

#print(X_train)
#print(X_test)

