from Application.Utils.AlgorithmDecorators import RegisterAlgorithm
from Application.Utils.OutputDecorators import OutputDialog

import numpy as np
import math


@RegisterAlgorithm("Hough", "Tools")
@OutputDialog(title="Output")
def hough(image):

   f=int(round(math.sqrt(image.shape[0]*image.shape[0]+image.shape[1]*image.shape[1]))+100)
   houghMap=np.zeros((f, 271), dtype=np.uint8)
   houghMap2 = np.zeros((f, 271), dtype=np.uint8)

   for k in range(1,image.shape[0]-1):
       for m in range(1,image.shape[1]-1):
            if(image[k,m]>10):
                for i in range(-90, 181):
                    r = m * math.cos(i * math.pi / 180) + k * math.sin(i * math.pi / 180)
                    if r>=0:
                        houghMap[math.floor(r), i + 90] += 1

   for i in range(0, houghMap2.shape[0]):
       for j in range(0, houghMap2.shape[1]):
           if (houghMap[i, j] >= 150):
               houghMap2[i, j] = houghMap[i, j]
           if houghMap2[i, j] > 255:
               houghMap2[i, j] = 255



   for i in range(0, houghMap2.shape[0]-1):
       for j in range(0, houghMap2.shape[1]-1):
           if houghMap2[i, j] != 0:
               houghMap2[i-25:i+26, j-25:j+26] = 0
               houghMap2[i, j] = 255
   return houghMap2










