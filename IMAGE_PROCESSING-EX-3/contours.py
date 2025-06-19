import cv2
import numpy as np

def contours():
    img = cv2.imread('input_image.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7,7), 0)
    
    # Edge detection and find contours
    edges = cv2.Canny(blurred, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw contours on original image
    result = img.copy()
    cv2.drawContours(result, contours, -1, (0,255,0), 2)
    
    cv2.imshow('Contours Detection', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

contours()