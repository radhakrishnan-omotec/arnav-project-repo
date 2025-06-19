import cv2

def Thresholding_Images():
    img = cv2.imread('input_image.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow("Thresholded Image", binary)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

Thresholding_Images()
