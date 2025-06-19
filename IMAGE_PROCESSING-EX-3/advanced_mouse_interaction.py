import cv2
import numpy as np

def advanced_mouse_interaction_logic():
    img = cv2.imread('input_image.jpg')
    clone = img.copy()
    
    # Mouse callback function
    def draw_rectangle(event, x, y, flags, param):
        nonlocal img, clone
        if event == cv2.EVENT_LBUTTONDOWN:
            clone = img.copy()
            cv2.rectangle(img, (x-50, y-50), (x+50, y+50), (0,255,0), 2)
        elif event == cv2.EVENT_RBUTTONDOWN:
            img = clone.copy()
    
    cv2.namedWindow("Advanced Mouse Interaction")
    cv2.setMouseCallback("Advanced Mouse Interaction", draw_rectangle)
    
    while True:
        cv2.imshow("Advanced Mouse Interaction", img)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC key
            break
    
    cv2.destroyAllWindows()

advanced_mouse_interaction_logic()