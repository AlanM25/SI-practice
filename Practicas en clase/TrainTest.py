from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris = load_iris()
data, labels = iris.data, iris.target

res = train_test_split(data, labels,
                       train_size=0.8,
                       test_size=0.2,
                       random_state=42)
train_data, test_data, train_labels, test_labels = res

print(train_data.shape)
print(test_data.shape)

n = 7
print(f"The first {n} data sets:")
print(test_data[:7])
print(f"The corresponding {n} labels:")
print(test_labels[:7])

exit()

import numpy as np
from sklearn.datasets import load_iris
iris = load_iris()

print(iris.target)

indices = np.random.permutation(len(iris.data))
print(indices)

n_test_samples = 12
learnset_data = iris.data[indices[:-n_test_samples]]
learnset_labels = iris.target[indices[:-n_test_samples]]
testset_data = iris.data[indices[-n_test_samples:]]
testset_labels = iris.target[indices[-n_test_samples:]]
print(learnset_data[:4], learnset_labels[:4])
print(testset_data[:4], testset_labels[:4])

exit()

import numpy as np
from sklearn.model_selection import train_test_split

file_data = np.loadtxt("resources/squirrels.txt")

data = file_data[:,:-1]
labels = file_data[:,-1]

data_sets = train_test_split(data,
                       labels,
                       train_size=0.8,
                       test_size=0.2,
                       random_state=42 # garantees same output for every run
                      )

train_data, test_data, train_labels, test_labels = data_sets
print(data.shape)
print(train_data.shape)
print(test_data.shape)