from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier, RadiusNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.datasets import load_digits, load_iris, load_wine, fetch_olivetti_faces

def Fake():
    n_classes = 6
    data, labels = make_blobs(n_samples=1000,
                              centers=n_classes,
                              cluster_std = 1.3,
                              random_state=1)

    colours = ('green', 'red', 'blue', 'magenta', 'yellow', 'pink')

    fig, ax = plt.subplots()
    for n_class in range(0, n_classes):
        ax.scatter(data[labels==n_class, 0], data[labels==n_class, 1],
                   c=colours[n_class], s=10, label=str(n_class))

#digits = load_digits()
#digits = load_iris()
digits = load_wine()
#digits = fetch_olivetti_faces()

data = digits.data
labels = digits.target

res = train_test_split(data, labels,
                       train_size=0.7,
                       test_size=0.3,
                       random_state=1)
train_data, test_data, train_labels, test_labels = res

print(len(train_data), len(test_data), len(train_labels))

X, Y = [], []
Radio = 1.0

while (True):
    try:
        classifier = RadiusNeighborsClassifier(radius=Radio)
        classifier.fit(train_data, train_labels)
        predictions = classifier.predict(test_data)
    except ValueError:
        Radio+=0.1
    else:
        break

print("Valor del Radio", Radio)

for k in range(1, 10):
    #classifier = KNeighborsClassifier(n_neighbors=k,
    #                                  p=2,  # Euclidian
    #                                  metric="minkowski")
    classifier = RadiusNeighborsClassifier(radius=Radio)
    classifier.fit(train_data, train_labels)
    predictions = classifier.predict(test_data)
    score = accuracy_score(test_labels, predictions)
    #X.append(k)
    X.append(Radio)
    Y.append(score)
    Radio += 0.5

fig, ax = plt.subplots()
ax.set_xlabel('k')
ax.set_ylabel('accuracy')
ax.plot(X, Y, "g-.o")
maxim = max(Y)
print("Valor de K con mayor exactitud", X[Y.index(maxim)], maxim)
plt.show()