import cv2
import numpy as np

def bounding_rectangle():
    img = cv2.imread('input_image.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # Find contours and get largest one
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_cnt = max(contours, key=cv2.contourArea)
    
    # Get bounding rectangle and draw it
    x,y,w,h = cv2.boundingRect(largest_cnt)
    result = img.copy()
    cv2.rectangle(result, (x,y), (x+w,y+h), (0,255,0), 3)
    
    cv2.imshow('Bounding Rectangle', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

bounding_rectangle()