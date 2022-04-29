from datasets import training_dataset_2
from network import Network

network = Network(structure=([3, 1]), activation='lineal', seed=17)
network.train(training_dataset_2, epochs=1000)

print(network.error(training_dataset_2))