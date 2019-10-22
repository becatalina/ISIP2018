from Application.Utils.AlgorithmDecorators import RegisterAlgorithm
from Application.Utils.InputDecorators import InputDialog
from Application.Utils.OutputDecorators import OutputDialog

import numpy

@RegisterAlgorithm("Binarizare2", "Thresholding")
@InputDialog(threshold1=int, threshold2=int)
@OutputDialog(title="Binarization Output")

def binarization(image, threshold1, threshold2):
    if len(image.shape) == 2:
        if threshold1 > threshold2:
            threshold1, threshold2 = threshold2, threshold1

        image[numpy.logical_or(image < threshold1, image > threshold2)] = 0
        image[numpy.logical_and(image >= threshold1, image <= threshold2)] = 255
        return image
    else:
        return "Error: image is not grayscale!"
