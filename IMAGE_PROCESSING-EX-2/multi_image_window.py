import cv2
import numpy as np

def Creating_a_Multi_Image_Window():
    img = cv2.imread('input_image.jpg')
    img_resized = cv2.resize(img, (200, 200))

    top_row = np.hstack((img_resized, img_resized))
    bottom_row = np.hstack((img_resized, img_resized))
    grid = np.vstack((top_row, bottom_row))

    cv2.imshow("Multi Image Grid", grid)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

Creating_a_Multi_Image_Window()