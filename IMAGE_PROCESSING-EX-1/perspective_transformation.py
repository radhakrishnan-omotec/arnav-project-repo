import cv2
import numpy as np

def Perspective_Transformation(img, src_points, dst_points):
    """Apply perspective transformation to warp the image."""
    # Get perspective transform matrix
    matrix = cv2.getPerspectiveTransform(src_points, dst_points)
    # Apply the transformation
    warped = cv2.warpPerspective(img, matrix, (img.shape[1], img.shape[0]))
    return warped

# Load the image
img = cv2.imread('input_image.jpg')
if img is None:
    raise FileNotFoundError("input_image.jpg not found")

# Define source and destination points for perspective transform
h, w = img.shape[:2]
src_points = np.float32([[0, 0], [w, 0], [w, h], [0, h]])  # Corners of the image
dst_points = np.float32([[0, 0], [w, 0], [w*0.8, h], [w*0.2, h]])  # Trapezoid shape

# Apply perspective transformation
result = Perspective_Transformation(img, src_points, dst_points)

# Display and save the result
cv2.imshow('Perspective Transformation', result)
cv2.imwrite('perspective_output.jpg', result)
cv2.waitKey(0)
cv2.destroyAllWindows()