import numpy as np
import argparse
import cv2

# ap = argparse.ArgumentParser()
# ap.add_argument("-i",'--image', required = True, help = "Path to the image")
# args = vars(ap.parse_args())

image = cv2.imread("cir2.png")
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 91, 1)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 5, 200)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")

    for (x, y, r) in circles:

        cv2.circle(output, (x,y), r, (0, 255, 0), 4)
        cv2.rectangle(output, (x-5, y-5), (x+5, y+5), (0, 128, 255), -1)

    cv2.imshow("output", np.hstack([image, output]))
    cv2.waitKey(0)