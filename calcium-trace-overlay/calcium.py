from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

im = Image.open("transillumination.png")
img = mpimg.imread("transillumination.png")
imgplot = plt.imshow(img)

input()

draw = ImageDraw.Draw(im)
draw.ellipse([10, 10, 20, 20], outline=(255, 255, 255), width=5)

imgplot = plt.imshow(img)
    