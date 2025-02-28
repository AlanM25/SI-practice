from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits

digits = load_digits()
data = digits.data
labels = digits.target

res = train_test_split(data, labels,train_size=0.8,random_state=1)
train_data, test_data, train_labels, test_labels = res

# Create and fit a nearest-neighbor classifier
from sklearn.neighbors import KNeighborsClassifier, RadiusNeighborsClassifier

# Instantiate the RadiusNeighborsClassifier
rnc = RadiusNeighborsClassifier(radius=50.0)
knn = KNeighborsClassifier()

rnc.fit(train_data, train_labels)
knn.fit(train_data, train_labels)

from sklearn.metrics import accuracy_score, confusion_matrix

predictedA = knn.predict(test_data)
print("Predictions from the classifier KNN:")
#print(predictedA)
print("Target values:")
#print(test_labels)
print("Precision Prueba: ", accuracy_score(predictedA, test_labels))
print("Precision Prueba: ", accuracy_score(predictedA,
                     test_labels,
                     normalize=False))
cmA = confusion_matrix(predictedA, test_labels)
print(cmA)

predictedA = rnc.predict(test_data)
print("Predictions from the classifier RNC:")
#print(predictedB)
print("Target values:")
#print(test_labels)
print("Precision Prueba: ", accuracy_score(predictedA, test_labels))
print("Precision Prueba: ", accuracy_score(predictedA,
                     test_labels,
                     normalize=False))
cmB = confusion_matrix(predictedA, test_labels)
print(cmB)



