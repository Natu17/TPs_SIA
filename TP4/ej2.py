from alphabet import alphabet
from hopfield import Hopfield
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(1)

def noise(pattern, p):
    noise = rng.random(patterns.shape[1])
    noise[noise >= p] = 1
    noise[noise < p] = -1
    return noise*pattern

def identify_pattern(patterns, pattern):
    for i,p in enumerate(patterns):
        if not (p-pattern).any():
            return i
    
    return -1



network = Hopfield()

patterns = np.array([ np.array(pattern).ravel() for pattern in alphabet.values()])

chars = ["H", "I", "L", "X"]

idx = [ list(alphabet.keys()).index(char) for char in chars]

patterns = patterns[idx]

patterns[patterns == 0] = -1


network.train(patterns)

fake_states =[]

for i in range(2**10):
    idx = i%len(patterns)
    pattern = patterns[idx]
    noise_pattern = noise(pattern, 0.5)
    prediction = network.predict(noise_pattern)
    idx = identify_pattern(patterns, prediction)
    if idx == -1:
        fake_states.append([prediction, pattern])

fake_states, count = np.unique(fake_states, axis=0, return_counts=True)
##print(fake_states)
#print(count)
#print(len(fake_states))

# for a,p in zip(chars, patterns):
#         plt.figure(str(a))
#         plt.title(str(a))
#         plt.imshow(p.reshape(5,5), cmap='winter')



i=0
for state, c in zip(fake_states, count):
    if c < 5:
        continue

    fig,ax =plt.subplots(1,2, figsize=(10,5))
    ax[0].set_title("count: " +  str(c))
    ax[0].imshow(state[0].reshape(5,5), cmap='winter')
    ax[0].set_axis_off()
    ax[1].imshow(state[1].reshape(5,5), cmap='winter')
    ax[1].set_axis_off()
    i+=1

    plt.savefig("fake_states_{}.png".format(i))