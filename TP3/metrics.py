import numpy
from network import Network
import copy

def cross_validation(dataset, network_template, seed,k,epochs):
    
    if len(dataset) % k != 0:
        raise ValueError("dataset must be divisible by k")

    n = int(len(dataset)/k)
    start = 0
    end = n
    test = dataset[start : end]
    training = dataset[end:]
    
    while(end <= len(dataset)):
        network = copy.deepcopy(network_template)
        network.train(training, epochs)
        #metodo validacion test
   
        start = end
        end+=n
        test = dataset[start : end]
        training = dataset[:start] + dataset[end : ]
       
def metrics(dataset):
        
        