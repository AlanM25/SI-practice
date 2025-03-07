from sklearn.datasets import make_blobs
import numpy as np

n_samples = 300
samples, labels = make_blobs(n_samples=n_samples,
                             centers=([2, 6], [6, 2]),
                             random_state=0)

import matplotlib.pyplot as plt

colours = ('green', 'red', 'blue', 'magenta', 'yellow', 'cyan')
fig, ax = plt.subplots()

for n_class in range(2):
    ax.scatter(samples[labels == n_class][:, 0], samples[labels == n_class][:, 1],
               c=colours[n_class], s=40, label=str(n_class))
plt.show()
size_of_learn_sample = int(n_samples * 0.8)
size_of_test_sample = n_samples - size_of_learn_sample

learn_data = samples[:size_of_learn_sample]
test_data = samples[-size_of_test_sample:]

learn_labels = labels[:size_of_learn_sample]
test_labels = labels[-size_of_test_sample:]

from neural_network_softmax import NeuralNetwork

simple_network = NeuralNetwork(no_of_in_nodes=2, 
                               no_of_out_nodes=2, 
                               no_of_hidden_nodes=5,
                               learning_rate=0.3,
                               softmax=True)

#for x in [(1, 4), (2, 6), (3, 3), (6, 2)]:
#    y = simple_network.run(x)
#    print(x, y, s.sum())

#labels_one_hot = (np.arange(2) == labels.reshape(labels.size, 1))
labels_one_hot = (np.arange(2) == learn_labels.reshape(size_of_learn_sample, 1))
labels_one_hot = labels_one_hot.astype(np.float64)

for i in range(size_of_learn_sample):
    # print(learn_data[i], labels[i], labels_one_hot[i])
    simple_network.train(learn_data[i],
                         labels_one_hot[i])

from collections import Counter
evaluation = Counter()
print(len(learn_data))
print(len(test_data))

print(simple_network.evaluate(learn_data, learn_labels))
print(simple_network.evaluate(test_data, test_labels))