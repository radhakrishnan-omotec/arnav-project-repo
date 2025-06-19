import cv2
import numpy as np

def Contours(img):
    """Detect and draw contours on the image."""
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply edge detection
    edges = cv2.Canny(gray, 100, 200)
    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw contours on a copy of the original image
    result = img.copy()
    cv2.drawContours(result, contours, -1, (0, 255, 0), 2)
    return result

# Load the image
img = cv2.imread('input_image.jpg')
if img is None:
    raise FileNotFoundError("input_image.jpg not found")

# Detect and draw contours
result = Contours(img)

# Display and save the result
cv2.imshow('Contours', result)
cv2.imwrite('contours_output.jpg', result)
cv2.waitKey(0)
cv2.destroyAllWindows()