import cv2
import numpy as np

def Thresholding_Images(img):
    """Apply adaptive thresholding to create a binary image."""
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply adaptive thresholding
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY, 11, 2)
    # Convert thresholded image to BGR for display
    result = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
    return result

# Load the image
img = cv2.imread('input_image.jpg')
if img is None:
    raise FileNotFoundError("input_image.jpg not found")

# Apply thresholding
result = Thresholding_Images(img)

# Display and save the result
cv2.imshow('Thresholding Images', result)
cv2.imwrite('threshold_output.jpg', result)
cv2.waitKey(0)
cv2.destroyAllWindows()