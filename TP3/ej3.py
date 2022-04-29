from network import Network
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import os


def a():

    lim = 1
    size = 50
    x = np.linspace(-lim, lim, size)
    y = np.linspace(-lim, lim, size)
    sample = [[i, j] for i in x for j in y]

    frame = 0

    mesh = plt.pcolormesh(x, y, np.zeros((size, size)),
                          shading='gouraud', vmin=-1, vmax=1)

    
    dataset = [
        [[-1, -1], [-1]],
        [[-1, 1], [1]],
        [[1, -1], [1]],
        [[1, 1], [-1]]
    ]
    
    #errors = []
    imgs = []

    def update(i):
        img = imgs[i]
        print("\rprogress: {:.2f}%".format(100*(i+1)/len(imgs)), end="")
        mesh.set_array(img.ravel())
        return mesh

    def add_img(network):
        img = np.zeros((size, size))
        for i in range(size):
            for j in range(size):
                img[i][j] = network.feedforward([x[i], y[j]])[0]

        imgs.append(img)




    network = Network(structure=(
        [2, 3, 2, 1]), activation='tanh', seed=1, args={'b': 1})
    network.train(dataset, learning_rate=0.01, momentum=0,
                  target_error=0.1, callback=add_img)

    #plt.plot(errors)
    #plt.yscale('log')
    #plt.show()
    #os.system('ffmpeg -framerate 15 -i tmp_%08d.png -vcodec mpeg4 -y output.mp4')
   # os.system('rm tmp_*.png 2> /dev/null')

    anim = animation.FuncAnimation(plt.gcf(),update, frames = len(imgs), interval=70)

    anim.save('output.mp4', writer='ffmpeg')

if __name__ == "__main__":
    a()
