import cv2
import numpy as np

def Bounding_Rectangle(img):
    """Detect the largest contour and draw its minimum bounding rectangle."""
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply edge detection
    edges = cv2.Canny(gray, 100, 200)
    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Find the largest contour by area
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        # Get the minimum bounding rectangle
        rect = cv2.minAreaRect(largest_contour)
        box = cv2.boxPoints(rect)
        box = np.intp(box)
        
        # Draw the rectangle on a copy of the image
        result = img.copy()
        cv2.drawContours(result, [box], 0, (0, 255, 0), 2)
        return result
    return img  # Return original if no contours found

# Load the image
img = cv2.imread('input_image.jpg')
if img is None:
    raise FileNotFoundError("input_image.jpg not found")

# Detect and draw bounding rectangle
result = Bounding_Rectangle(img)

# Display and save the result
cv2.imshow('Bounding Rectangle', result)
cv2.imwrite('bounding_rectangle_output.jpg', result)
cv2.waitKey(0)
cv2.destroyAllWindows()