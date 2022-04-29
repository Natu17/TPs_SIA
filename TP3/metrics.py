import numpy
import random
from network import Network

def cross_validation(dataset, structure, activation, seed,k,epochs):
    start = 0
    end = k
    test = dataset[start : end]
    training = dataset[end:]
    while(end >= dataset.size()):
        network = Network(structure, activation, seed)
        network.train(training, epochs)
        #metodo validacion test
        start = end
        end+=k
        test = dataset[start : end]
        training = dataset[:start] + dataset[end : ]
    