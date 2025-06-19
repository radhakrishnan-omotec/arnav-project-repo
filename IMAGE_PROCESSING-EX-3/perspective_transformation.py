import cv2
import numpy as np

def perspective_transformation():
    img = cv2.imread('input_image.jpg')
    h, w = img.shape[:2]
    
    # Source points (book corners)
    src = np.float32([[0,0], [w,0], [0,h], [w,h]])
    # Destination points (perspective shift)
    dst = np.float32([[0,0], [w-100,50], [50,h-50], [w-50,h-100]])
    
    # Get perspective matrix and warp image
    matrix = cv2.getPerspectiveTransform(src, dst)
    result = cv2.warpPerspective(img, matrix, (w, h))
    
    cv2.imshow('Original', img)
    cv2.imshow('Perspective Transformation', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

perspective_transformation()