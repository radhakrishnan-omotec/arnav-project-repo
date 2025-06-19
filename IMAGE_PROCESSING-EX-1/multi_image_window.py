import cv2
import numpy as np

def Creating_Multi_Image_Window(img):
    """Create a single window with original, grayscale, blurred, and edge-detected images."""
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    # Detect edges using Canny
    edges = cv2.Canny(gray, 100, 200)
    
    # Convert grayscale and edges to BGR for stacking
    gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    
    # Resize images to the same height for stacking
    height = img.shape[0]
    images = [img, gray_bgr, blurred, edges_bgr]
    resized_images = [cv2.resize(im, (int(im.shape[1] * height / im.shape[0]), height)) for im in images]
    
    # Stack images horizontally
    multi_image = np.hstack(resized_images)
    return multi_image

# Load the image
img = cv2.imread('input_image.jpg')
if img is None:
    raise FileNotFoundError("input_image.jpg not found")

# Create multi-image window
result = Creating_Multi_Image_Window(img)

# Display and save the result
cv2.imshow('Multi-Image Window', result)
cv2.imwrite('multi_image_output.jpg', result)
cv2.waitKey(0)
cv2.destroyAllWindows()