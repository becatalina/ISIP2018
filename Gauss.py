from Application.Utils.AlgorithmDecorators import RegisterAlgorithm

import numpy as np

@RegisterAlgorithm("Gauss3", "Filter")
def Gauss(image):
    sigma = 3
    n = 13
    e = 2.718
    mask = np.ndarray(shape=(13, 13))
    coef = 1/(2*np.pi*(sigma**2))
    s = 0
    for i in range(-6, 7):
        for j in range(-6, 7):
            mask[i+6, j+6] = coef*(e**((-(i**2 + j**2))/(2*(sigma**2))))
            s += mask[i+6, j+6]
    mask /= s

    for i in range(6, image.shape[0]-7):
        for j in range(6, image.shape[1]-7):
            image[i, j] = int(np.sum(image[i-6:i+7, j-6:j+7]*mask))

    return image















