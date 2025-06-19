import cv2
import numpy as np

# Global variables to store points
points = []

def Advanced_Mouse_Interaction(event, x, y, flags, param):
    """Handle mouse events to draw points and lines on the image."""
    global points
    img = param[0].copy()  # Work on a copy of the image
    
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        cv2.circle(img, (x, y), 5, (0, 255, 0), -1)  # Draw a green dot
        cv2.putText(img, f'({x}, {y})', (x + 10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        # Draw lines between consecutive points
        if len(points) > 1:
            cv2.polylines(img, [np.array(points)], False, (0, 0, 255), 2)
        
        cv2.imshow('Advanced Mouse Interaction', img)

# Load the image
img = cv2.imread('input_image.jpg')
if img is None:
    raise FileNotFoundError("input_image.jpg not found")

# Create a window and set the mouse callback
cv2.namedWindow('Advanced Mouse Interaction')
cv2.setMouseCallback('Advanced Mouse Interaction', Advanced_Mouse_Interaction, [img])

# Display the image and wait for a key press
cv2.imshow('Advanced Mouse Interaction', img)
cv2.waitKey(0)
cv2.destroyAllWindows()