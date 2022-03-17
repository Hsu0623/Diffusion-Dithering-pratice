# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 19:13:21 2019

@author: User
"""

import cv2
import numpy as np
origin = cv2.imread("D:\\hw_picture\\lena.jpg",0)

error_array = np.array(
[[0.0,   0.0,     0.0,     0.19040, 0.095230],
[0.04762,0.095230,0.19040, 0.095230,0.04762],
[0.02381,0.047620,0.095230,0.047620,0.02381]])

rs, cs = origin.shape
halftone = np.zeros((rs+2,cs+4))
halftone[0: rs,2:cs+2] = origin

for i in range(0, rs):
    for j in range(2,cs+2):
        old = halftone[i][j]
        halftone[i][j] = (old//128)*255
        E = old - (255*(old//128))
        halftone[i:i+3,j-2:j+3] += E*error_array
        

outimage = halftone[0:rs, 2:cs+2]
cv2.imwrite("D:\\hw_picture\\lena_error_diffusion.jpg", outimage)
image = cv2.imread("D:\\hw_picture\\lena_error_diffusion.jpg", 0)
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
