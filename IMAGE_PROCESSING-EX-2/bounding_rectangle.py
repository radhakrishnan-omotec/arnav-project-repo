import cv2

def Bounding_Rectangle():
    img = cv2.imread('input_image.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    img_copy = img.copy()
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img_copy, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Bounding Rectangles", img_copy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

Bounding_Rectangle()