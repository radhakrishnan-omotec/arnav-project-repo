import cv2
import numpy as np

def Perspective_Transformation():
    img = cv2.imread('input_image.jpg')
    rows, cols = img.shape[:2]

    src_points = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1], [cols - 1, rows - 1]])
    dst_points = np.float32([[50, 50], [cols - 100, 50], [50, rows - 100], [cols - 100, rows - 100]])

    matrix = cv2.getPerspectiveTransform(src_points, dst_points)
    warped = cv2.warpPerspective(img, matrix, (cols, rows))

    cv2.imshow("Perspective Transform", warped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

Perspective_Transformation()
