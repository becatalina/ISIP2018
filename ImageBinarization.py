

from Application.Utils.AlgorithmDecorators import RegisterAlgorithm



import numpy as np

@RegisterAlgorithm("Iterative Binarization", "Tools")


def IterativeBinarization(image):
    if len(image.shape) == 2:
        histogram = np.histogram(image, bins=range(257), range=(-1, 255))[0]
        rel_histogram = histogram/image.size
        threshold = 128
        while True:
            u0 = 0
            u1 = 0
            sum1 = 0
            for i in range(len(rel_histogram)):
                if i < threshold:
                    sum1 += rel_histogram[i]
                    u0 += i * rel_histogram[i]
                else:
                    u1 += i * rel_histogram[i]
            u0 /= sum1
            u1 /= (1-sum1)
            new_t = (u0+u1)//2
            if threshold == new_t:
                break
            else:
                threshold = new_t

        image[image < threshold] = 0
        image[image >= threshold] = 255
        return image
    else:
        return "Imaginea nu este greyscale"


