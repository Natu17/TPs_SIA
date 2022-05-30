import numpy as np

class Oja:
    def __init__(self, dataset, seed = 0):
        if seed:
            self.rng = np.random.default_rng(seed)
        else:
            self.rng = np.random.default_rng()

        self.dataset = dataset
        self.weights = self.rng.choice(dataset)

    def predict(self,x):
       return np.dot(self.weights,x)

    
    def train(self, epochs = 500, lr = 0.1, callback = None):

        for epoch in range(epochs):
            epoch_dataset = self.dataset.copy()
            self.rng.shuffle(epoch_dataset)
            for x in epoch_dataset:
                y = self.predict(x)
                self.weights += lr * (y*x -y**2 * self.weights)
            
            if callback:
                callback(self)

