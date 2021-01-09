import numpy as np
import argparse
import cv2
import tesseract

t2 = cv2.imread('cir2.png')
thresh = cv2.cvtColor(t2, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(thresh, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 91, 1)

print(tesseract.image_to_string(thresh))

# count, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh)
# for i in range(1,count):
#     t2 = cv2.circle(t2, (int(centroids[i,0]), int(centroids[i,1])), 5, (0, 255, 0, 0), 5)

cv2.imshow('circles', thresh)
cv2.imshow('centers', t2)
cv2.waitKey()