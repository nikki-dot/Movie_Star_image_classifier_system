import numpy as np
import pywt
import cv2

def w2d(img,mode="haar",level=1):
    imArray=img
    #convert to gray
    imArray=cv2.cvtColor(imArray,cv2.COLOR_RGB2GRAY)
    #convert to float
    imArray=np.float32(imArray)
    #divide by 255 to normalize pixel value
    imArray /= 255
    #wavedec2
    coeffs=pywt.wavedec2(imArray, mode, level=level)
    coeffs_H=list(coeffs)
    coeffs_H[0] *= 0
    #waverec2
    imArray_H=pywt.waverec2(coeffs,mode)
    imArray_H *=255
    imArray_H=np.uint8(imArray_H)
    return imArray_H