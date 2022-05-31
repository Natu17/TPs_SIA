from tabnanny import check
import numpy as np


def check_loop(arr, v):
    for i in range(len(arr)):
        if np.array_equal(arr[i], v):
            return True
    return False


class Hopfield:
    def __init__(self):
        pass

    def train(self, patterns):
                
        # Cada fila es una neurona, cada columna un peso
        self.weights = np.zeros((patterns.shape[1], patterns.shape[1]))
        
        for i in range(len(self.weights)-1):
            for j in range(i+1, len(self.weights)):

                # sumatoria de todos los patrones
                sum = 0
                for pattern in patterns:
                    sum += pattern[i] * pattern[j]

                self.weights[i, j] = self.weights[j, i] = sum/len(self.weights)

    def predict(self, input, callback=None):
        history = []

        while not check_loop(history, input):
            history.append(input)
            if callback: callback(self,input)
            product = np.dot(self.weights, input)
            
            input = np.array(input)
            
            for i in range(len(product)):
                if product[i] > 0:
                    input[i] = 1
                if product[i] < 0:
                    input[i] = -1

            

        return input
