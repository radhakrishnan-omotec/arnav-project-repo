import cv2
import numpy as np

def thresholding_images():
    img = cv2.imread('input_image.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply different thresholding techniques
    _, thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    _, thresh2 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    _, thresh3 = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
    thresh4 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY, 11, 2)
    
    # Display results
    cv2.imshow('Original', img)
    cv2.imshow('Binary Threshold', thresh1)
    cv2.imshow('Inverse Threshold', thresh2)
    cv2.imshow('Truncated Threshold', thresh3)
    cv2.imshow('Adaptive Threshold', thresh4)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

thresholding_images()