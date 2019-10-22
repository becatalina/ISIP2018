from Application.Utils.AlgorithmDecorators import RegisterAlgorithm
from Application.Utils.InputDecorators import InputDialog

import numpy as np


@RegisterAlgorithm("Roberts", "Filter")
@InputDialog(threshold=int)
def roberts(image, threshold):
    t = threshold
    imageaux = image.copy().astype(np.int32)
    image2 = image.copy().astype(np.int32)
    image3 = image.copy().astype(np.int32)

    for i in range(1, imageaux.shape[0]-1):
        for j in range(1, imageaux.shape[1]-1):
            image2[i, j] = 2*imageaux[i+1, j-1]-2*imageaux[i-1, j+1] + imageaux[i, j-1] - imageaux[i-1, j] + imageaux[i+1, j] - imageaux[i,j+1]
            image3[i, j] = 2*imageaux[i+1, j+1]-2*imageaux[i-1, j-1] + imageaux[i, j+1] - imageaux[i-1, j] + imageaux[i+1, j] - imageaux[i,j-1]

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            grad = np.sqrt(image2[i, j]**2 + image3[i, j]**2)
            if grad <= t:
                image[i, j] = 0
            else:
                image[i, j] = 255

    return image.astype(np.uint8)










