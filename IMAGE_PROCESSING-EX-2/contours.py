import cv2

def Contours():
    img = cv2.imread('input_image.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 50, 150)
    contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    img_contours = img.copy()
    cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 2)

    cv2.imshow("Contours", img_contours)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

Contours()