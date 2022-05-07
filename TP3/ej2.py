from datasets import training_dataset_2
from network import Network
import metrics as m


# expected = [y[0] for x, y in training_dataset_2]
# network = Network(structure=([3, 1]),
#                   activation='lineal', seed=17, args={'b': 0.1})    
         
# p = m.cross_validation(training_dataset_2, network, k=5,  epochs=100, metric = lambda n,d: m.accuracy(n,d,10))
# print(p[0])
# print(p[1])


expected = [y[0] for x, y in training_dataset_2]

max_value = max(expected)
min_value = min(expected)

delta = (max_value - min_value)/2

normalized = []

for (x, y), v in zip(training_dataset_2, expected):
    e = (v - min_value)/delta - 1
    normalized.append((x, [e]))

network = Network(structure=([3, 1]), activation='tanh', seed=17)
p = m.cross_validation(normalized, network, k=5,  epochs=20, metric = lambda n,d: m.accuracy(n,d, 1e-5))
print(p[0].w)
print(p[1])