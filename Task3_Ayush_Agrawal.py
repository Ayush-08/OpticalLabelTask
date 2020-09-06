import cv2
import numpy as np

img= cv2.imread(r"C:\Users\Ayush Agrawal\Desktop\ChessACM.jpg")
#cv2.imshow('Original Image', img)

height, width= img.shape[0:2]
bottom = img[height-2:height, 0:width]
mean = cv2.mean(bottom)[0]

gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Gray image',gray)
#cv2.waitKey(0)

sobelx= cv2.Sobel(gray, cv2.CV_64F, 0,1, ksize=3)
#cv2.imshow('sobelx', sobelx)
border = cv2.copyMakeBorder(
    sobelx,
    top = int(0.25 * img.shape[0]),  # shape[0] = rows
    bottom = int(0.25 * img.shape[0]),
    left = int(0.1 * img.shape[1]),  # shape[1] = cols
    right = int(0.1 * img.shape[1]),
    borderType=cv2.BORDER_WRAP,
    value=[mean, mean, mean]
)

#cv2.imshow('border', border)
#cv2.waitKey(0)



sobely= cv2.Sobel(border, cv2.CV_64F, 0,1, ksize=5)
#cv2.imshow('sobely', sobely)
border2 = cv2.copyMakeBorder(
    sobely,
    top = int(0.25 * img.shape[0]),  # shape[0] = rows
    bottom = int(0.25 * img.shape[0]),
    left = int(0.1 * img.shape[1]),  # shape[1] = cols
    right = int(0.1 * img.shape[1]),
    borderType=cv2.BORDER_WRAP,
    value=[mean, mean, mean]
)

#cv2.imshow('border2', border2)
#cv2.waitKey(0)

ret, thresh= cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

#cv2.imshow('Threshold', thresh)
#cv2.waitKey(0)



