import cv2
import numpy as np

def Painting_Transparency(img, alpha=0.5):
    """Apply transparency effect by blending the image with a solid color background."""
    # Create a solid color background (e.g., white)
    background = np.ones_like(img) * 255  # White background
    # Blend the image with the background using alpha
    transparent_img = cv2.addWeighted(img, alpha, background, 1 - alpha, 0)
    return transparent_img

# Load the image
img = cv2.imread('input_image.jpg')
if img is None:
    raise FileNotFoundError("input_image.jpg not found")

# Apply transparency
result = Painting_Transparency(img, alpha=0.7)

# Display and save the result
cv2.imshow('Painting Transparency', result)
cv2.imwrite('transparent_output.jpg', result)
cv2.waitKey(0)
cv2.destroyAllWindows()