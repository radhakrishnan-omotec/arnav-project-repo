import cv2

def Advanced_Mouse_Interaction_Logic():
    def mouse_event(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print(f"Left Click at: ({x}, {y})")
        elif event == cv2.EVENT_RBUTTONDOWN:
            print(f"Right Click at: ({x}, {y})")
        elif event == cv2.EVENT_MOUSEMOVE:
            print(f"Mouse Move: ({x}, {y})")

    img = cv2.imread('input_image.jpg')
    cv2.imshow("Mouse Interaction", img)
    cv2.setMouseCallback("Mouse Interaction", mouse_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

Advanced_Mouse_Interaction_Logic()