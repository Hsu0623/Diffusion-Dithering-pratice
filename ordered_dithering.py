# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 18:32:39 2019

@author: User
"""
import cv2
import numpy as np

origin = cv2.imread("D:\\hw_picture\\lena.jpg",0)
dithering_array = np.array(
 [[0.513,0.272,0.724,0.483,0.543,0.302,0.694,0.453],
 [0.151,0.755,0.091,0.966,0.181,0.758,0.121,0.936],
 [0.634,0.392,0.574,0.332,0.664,0.423,0.604,0.362],
 [0.060,0.875,0.211,0.815,0.030,0.906,0.241,0.845],
 [0.543,0.302,0.694,0.453,0.513,0.272,0.724,0.483],
 [0.181,0.758,0.121,0.936,0.151,0.755,0.091,0.936],
 [0.664,0.423,0.604,0.362,0.634,0.392,0.574,0.332],
 [0.030,0.906,0.241,0.845,0.060,0.875,0.211,0.815]])
da1 = np.tile(dithering_array,(64,64))

origin = origin / 255
origin[origin > da1] = 255
origin[origin <= da1] = 0

cv2.imwrite("D:\\hw_picture\\lena_dithering.jpg", origin)
image = cv2.imread("D:\\hw_picture\\lena_dithering.jpg",0)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()