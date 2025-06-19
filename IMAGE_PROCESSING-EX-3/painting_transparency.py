import cv2
import numpy as np

def painting_transparency():
    img = cv2.imread('input_image.jpg')
    overlay = img.copy()
    
    # Draw semi-transparent shapes
    cv2.rectangle(overlay, (100,100), (400,300), (0,0,255), -1)
    cv2.circle(overlay, (500,200), 80, (255,0,0), -1)
    
    alpha = 0.4  # Transparency factor
    cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)
    
    cv2.imshow('Painting Transparency', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

painting_transparency()