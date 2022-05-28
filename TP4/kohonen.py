import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

class Kohonen:

    def __init__(self, dataset, k = 6, seed = 0, initial_n = 1):        
        if seed:
            self.rng = np.random.RandomState(seed)
        else:
            self.rng = np.random.default_rng()

        self.weights = self.rng.choice (dataset, size=(k,k), replace=True)
        self.initital_radius = k * k
        self.dataset = dataset
        self.iteration_number = 0
        self.initial_n = initial_n
        self.k = k
    

    def iteration(self,x):
        self.iteration_number += 1
        radius = self.initital_radius / self.iteration_number if self.initital_radius > self.iteration_number else math.exp(self.initital_radius / self.iteration_number)
        n = self.initial_n/ (self.iteration_number)
        distances = np.linalg.norm(self.weights - x, axis=2)
        winner_pos = np.unravel_index(distances.argmin(), distances.shape)
        
        for i in range(self.k):
            for j in range(self.k):
                pos = np.array([i,j])
                distance = np.linalg.norm(winner_pos - pos)
                if distance < radius:
                    self.weights[i,j] +=  n*(x-self.weights[i,j])
     
    def train(self, epochs=0):
        if not epochs:
            epochs = len(self.dataset[0])*500

        for epoch in range(epochs):
            epoch_dataset = self.dataset.copy()
            self.rng.shuffle(epoch_dataset)

            for x in epoch_dataset:
                self.iteration(x)

    
        
    
if __name__ == "__main__":
    #loading data
    dataset = pd.read_csv('europe.csv')

    #le sacamos el nombre de los paises
    countries = dataset.iloc[:,0]
    variable_names = dataset.iloc[:,1:].columns
    variables = dataset.iloc[:, 1:].values



    standarized = (variables - variables.mean(axis=0))/variables.std(axis=0)

    network = Kohonen(standarized)

    network.train(epochs=100)

austria = variables[2]

v = np.linalg.norm(network.weights-austria, axis=2)

im = plt.imshow(v)

plt.colorbar(im)

plt.show()