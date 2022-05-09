from datasets import training_dataset_2
from network import Network
import metrics as m


expected = [y[0] for x, y in training_dataset_2]
network = Network(structure=([3, 1]),
                  activation='lineal', seed=17, args={'b': 0.1})    
         
p = m.cross_validation(training_dataset_2, network, k=5,  epochs=100, metric = lambda n,d: m.accuracy(n,d,10))
print(p[0])
print(p[1])


