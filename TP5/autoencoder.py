import network
import numpy as np

def autoencoder(font):
    encode = np.array([network.encode(IN) for IN in font])
    decode = np.array([network.decode(IN) for IN in font])