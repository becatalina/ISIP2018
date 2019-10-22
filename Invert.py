from Application.Utils.AlgorithmDecorators import RegisterAlgorithm


@RegisterAlgorithm("Inversare", "Tab2")
def Inversare(image):
    return 255 - image


import numpy


@RegisterAlgorithm("Flip", "Tab2")
def Flip(image):
    image[:, ] = numpy.flip(image, (0))
    image[:, ] = numpy.flip(image, (1))
    return image


@RegisterAlgorithm("Cut", "Tab2", fromMainModel=["rightClickLastPositions"])
def Crop(image, rightClickLastPositions):
    x = rightClickLastPositions[0]
    y = rightClickLastPositions[1]

    return image[x[0]:y[0], x[1]:y[1]]


