import cv2
import numpy as np

def creating_a_multi_image_window():
    img = cv2.imread('input_image.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    blurred = cv2.GaussianBlur(img, (15,15), 0)
    
    # Create canvas
    canvas = np.zeros((1000, 1500, 3), dtype=np.uint8)
    
    # Place images on canvas
    canvas[0:500, 0:750] = cv2.resize(img, (750,500))
    canvas[0:500, 750:1500] = cv2.resize(gray, (750,500))
    canvas[500:1000, 0:750] = cv2.resize(hsv, (750,500))
    canvas[500:1000, 750:1500] = cv2.resize(blurred, (750,500))
    
    # Add labels
    fonts = [cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 2]
    cv2.putText(canvas, "Original", (50,40), *fonts)
    cv2.putText(canvas, "Grayscale", (800,40), *fonts)
    cv2.putText(canvas, "HSV", (50,540), *fonts)
    cv2.putText(canvas, "Blurred", (800,540), *fonts)
    
    cv2.imshow('Multi-Image Dashboard', canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

creating_a_multi_image_window()