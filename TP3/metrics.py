import numpy as np
from network import Network
import copy


def cross_validation(dataset, network_template, k, epochs, metric, lr = 0.1, m=0):

    if len(dataset) % k != 0:
        raise ValueError("dataset must be divisible by k")

    n = int(len(dataset)/k)

    groups = []

    # for i in range(k):
    #     test = dataset[i*n:(i+1)*n]
    #     train = dataset[:i*n] + dataset[(i+1)*n:]
    #     groups.append((train,test))

    start = 0
    end = n
    test = dataset[start: end]
    training = dataset[end:]
    r_test_prec = 0
    r_training_set = 0
    r_network = 0
    r_test_set = 0
    while(end <= len(dataset)):
        network = copy.deepcopy(network_template)
        network.train(training, epochs=epochs, learning_rate=lr, momentum=m)
        p = metric(network, test)
        if p >= r_test_prec:
            r_test_prec = p
            r_network = network
            r_training_set = training
            r_test_set = test
        start = end
        end += n
        test = dataset[start: end]
        training = dataset[:start] + dataset[end:]
    r_training_prec = metric(r_network,r_training_set)
    return (r_network,
        r_test_prec,
        r_training_prec,
        r_test_set,
        r_training_prec)


def get_nearest_class(classes, value):
    distances = [np.linalg.norm(value - c) for c in classes]
    return distances.index(min(distances))


def confusion_matrix(classes, predicted, expected):
    matrix = np.zeros((len(classes)+1, len(classes)+1))

    for p, e in zip(predicted, expected):
        class_idx = classes.index(e)
        obtained_idx = get_nearest_class(classes, p)
        matrix[class_idx][obtained_idx] += 1

    for i in range(len(classes)):
        TP = matrix[i][i]
        FN = np.sum(matrix[i]) - TP
        FP = np.sum(matrix[:, i]) - TP
        p = TP/(TP + FP) if TP + FP != 0 else 0
        r = TP/(TP + FN) if TP + FN != 0 else 0
        matrix[-1][i] = p*100
        matrix[i][-1] = r*100

    submatrix = matrix[:-1, :-1]

    accuracy = np.trace(submatrix)/np.sum(submatrix)

    return matrix, accuracy


def accuracy(network, dataset, epsilon=0.1):
    good = 0
    bad = 0
    for i in range(len(dataset)):
        expected = dataset[i][1][0]
        o = network.feedforward(dataset[i][0])
        if (np.abs(expected-o) <= epsilon):
            good += 1
        else:
            bad += 1
    p = good/(good + bad)
    return p
