import numpy as np
from collections import Counter

np.random.seed(42)

def distance(instance1, instance2):
    """ Calculates the Eucledian distance between two instances"""
    return np.linalg.norm(np.subtract(instance1, instance2))

def get_neighbors(training_set,
                  labels,
                  test_instance,
                  k,
                  distance):
    """
    get_neighors calculates a list of the k nearest neighbors
    of an instance 'test_instance'.
    The function returns a list of k 3-tuples.
    Each 3-tuples consists of (index, dist, label)
    where
    index    is the index from the training_set,
    dist     is the distance between the test_instance and the
             instance training_set[index]
    distance is a reference to a function used to calculate the
             distances
    """
    distances = []
    for index in range(len(training_set)):
        dist = distance(test_instance, training_set[index])
        distances.append((training_set[index], dist, labels[index]))
    distances.sort(key=lambda x: x[1])
    neighbors = distances[:k]
    return neighbors

def vote_harmonic_weights(neighbors, all_results=True):
    class_counter = Counter()
    number_of_neighbors = len(neighbors)
    for index in range(number_of_neighbors):
        class_counter[neighbors[index][2]] += 1 / (index + 1)
    labels, votes = zip(*class_counter.most_common())
    # print(labels, votes)
    winner = class_counter.most_common(1)[0][0]
    votes4winner = class_counter.most_common(1)[0][1]
    if all_results:
        total = sum(class_counter.values(), 0.0)
        for key in class_counter:
            class_counter[key] /= total
        return winner, class_counter.most_common()
    else:
        return winner, votes4winner / sum(votes)

def vote_distance_weights(neighbors, all_results=True):
    class_counter = Counter()
    number_of_neighbors = len(neighbors)
    for index in range(number_of_neighbors):
        dist = neighbors[index][1]
        label = neighbors[index][2]
        class_counter[label] += 1 / (dist**2 + 1)
    labels, votes = zip(*class_counter.most_common())
    #print(labels, votes)
    winner = class_counter.most_common(1)[0][0]
    votes4winner = class_counter.most_common(1)[0][1]
    if all_results:
        total = sum(class_counter.values(), 0.0)
        for key in class_counter:
             class_counter[key] /= total
        return winner, class_counter.most_common()
    else:
        return winner, votes4winner / sum(votes)


def create_features(number_samples, *min_max_features):
    """ Creates an array with number_samples rows and len(min_max_features) columns """
    features = []
    for min_val, max_val,rounding in min_max_features:
        features.append(np.random.uniform(min_val, max_val, number_samples).round(rounding))
    result = np.column_stack(features)
    return result

num_apples, num_mangos, num_lemons = 150, 150, 150
sweetness = (10, 18, 0)
acidity = 3.4, 4, 2
weight = 140.0, 250.0, 0
apples = create_features(num_apples, sweetness, acidity, weight)
apples[:20] # The first 20 fruits

sweetness = (6, 14, 0)
acidity = 3.6, 6, 1       # should be between 5.8 and 6
weight = 100.0, 300.0, 0
mangos = create_features(num_mangos, sweetness, acidity, weight)

sweetness = (6, 12, 0)
acidity = 2.0, 2.6, 1
weight = 130, 170, 0
lemons = create_features(num_lemons, sweetness, acidity, weight)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Combine the data and create labels
X = np.vstack((apples, mangos, lemons))
y = np.array(['Apple'] * num_apples + ['Mango'] * num_mangos + ['Lemon'] * num_lemons)

print(X)
print(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

import pandas as pd

# Define the DataFrame
df = pd.DataFrame(X, columns=['Sweetness', 'Acidity', 'Weight'])
df['Fruit'] = y

n_test_samples = len(X_test)

for i in range(20):
    neighbors = get_neighbors(X_train,
                              y_train,
                              X_test[i],
                              6,
                              distance=distance)

    print("index: ", i,
          ", result of vote: ",
          vote_harmonic_weights(neighbors,
                                all_results=True))


def evaluate(X_train, X_test, y_train, y_test, threshold=0):
    """
    Evaluate the performance of a K-nearest neighbors classifier.

    Parameters:
        X_train (ndarray): Training features.
        X_test (ndarray): Testing features.
        y_train (ndarray): Training labels.
        y_test (ndarray): Testing labels.
        threshold (float): Threshold for decision-making confidence (default: 0).
                           If the probability of the predicted class is below this threshold,
                           the sample will be marked as undecided.

    Returns:
        dict: A dictionary containing counts of correct predictions, wrong predictions,
              and undecided predictions.

    Note:
        The function assumes that there is another function called get_neighbors that
        retrieves the k-nearest neighbors for each sample, and the distance metric used
        by the K-nearest neighbors algorithm is defined in a variable called 'distance'.
    """
    evaluation = dict(corrects=0, wrongs=0, undecided=0)
    n_test_samples = len(X_test)
    for i in range(n_test_samples):
        neighbors = get_neighbors(X_train,
                                  y_train,
                                  X_test[i],
                                  6,
                                  distance=distance)
        class_label, probability = vote_distance_weights(neighbors, all_results=False)
        if class_label == y_test[i]:
            if probability >= threshold:
                evaluation['corrects'] += 1
            else:
                evaluation['undecided'] += 1
        else:
            if probability >= threshold:
                evaluation['wrongs'] += 1
            else:
                evaluation['undecided'] += 1
    return evaluation

R = evaluate(X_train, X_test, y_train, y_test, 0.5)
print(R)
R = evaluate(X_train, X_train, y_train, y_train, 0.5)
print(R)

exit()

Total = X_test.shape[0]
print("Exactitud", R['corrects']*100/Total)
print("Error", (R['wrongs']+R['undecided'])*100/Total)

print(R['corrects'])
print(R['wrongs'])
print(R['undecided'])
