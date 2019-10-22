from Application.Utils.AlgorithmDecorators import RegisterAlgorithm

import numpy as np

@RegisterAlgorithm("Morpho", "EdgeImage")
def morpho(image):

    imageaux = image.copy().astype(np.int32)
    for i in range(1, imageaux.shape[0] - 1):
        for j in range(1, imageaux.shape[1] - 1):
            s = np.sum(image[i-1:i+2, j-1:j+2])
            if s >= 255:
                imageaux[i, j] = 255
            else:
                imageaux[i, j] = 0


    #return imageaux.astype(np.uint8)

    for i in range(1, imageaux.shape[0]):
        for j in range(1, imageaux.shape[1]):
            if imageaux[i, j] != image[i, j]:
                imageaux[i, j] = 255
            else:
                imageaux[i, j] = 0


    return imageaux.astype(np.uint8)










