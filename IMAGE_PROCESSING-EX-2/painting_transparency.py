import cv2

def Painting_Transparency():
    img = cv2.imread('input_image.jpg')
    overlay = img.copy()
    output = img.copy()

    cv2.rectangle(overlay, (50, 50), (300, 300), (0, 255, 0), -1)
    alpha = 0.4  # Transparency factor
    cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)

    cv2.imshow("Transparent Overlay", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

Painting_Transparency()