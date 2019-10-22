from Application.Utils.AlgorithmDecorators import RegisterAlgorithm
from Application.Utils.OutputDecorators import OutputDialog

from numpy import *


@RegisterAlgorithm("G-AdaptSobel", "Filter")
@OutputDialog(title="Output")
def function(image):

    H_y = asarray([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    H_x = asarray([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    x_applied = y_applied = zeros(image.shape)
    for row in range(1, image.shape[0] - 1):
        for column in range(1, image.shape[1] - 1):
            x_applied[row, column] = sum(image[row - 1:row + 2, column - 1:column + 2] * H_x)
            y_applied[row, column] = sum(image[row - 1:row + 2, column - 1:column + 2] * H_y)
    filtered=(sqrt(x_applied ** 2 + y_applied ** 2))

    gmax = amax(filtered)

    threshold = gmax // 2

    filtered[filtered < threshold] = 0
    filtered[filtered >= threshold] = 255

    return filtered.astype(uint8)
