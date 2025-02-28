import cv2
import numpy as np

image = cv2.imread('input_image.jpg', 0)

# Print error message if image is null
if image is None:
    print('Could not read image')

# Apply identity kernel
kernel1 = np.array([[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])

identity = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)

cv2.imshow('Original', image)
#cv2.imshow('Identity', identity)

#cv2.waitKey()
#cv2.imwrite('identity.jpg', identity)
#cv2.destroyAllWindows()

# Apply blurring kernel
kernel2 = np.ones((5, 5), np.float32) / 25
print(kernel2)
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)

#kernel3 = np.ones((9, 9), np.float32) / 81
#print(kernel3)
#img2 = cv2.filter2D(src=image, ddepth=-1, kernel=kernel3)

gaussian_blur = cv2.GaussianBlur(src=image, ksize=(5,5),sigmaX=0, sigmaY=0)

median = cv2.medianBlur(src=image, ksize=5)

kernel3 = np.array([[0, -1,  0],
                   [-1,  5, -1],
                    [0, -1,  0]])
sharp_img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel3)

bilateral_filter = cv2.bilateralFilter(src=image, d=9, sigmaColor=75, sigmaSpace=75)

# Basic threhold example
#th, dst = cv2.threshold(image, 64, 255, cv2.THRESH_BINARY);
th, dst = cv2.threshold(bilateral_filter, 64, 255, cv2.THRESH_BINARY);
#cv2.imwrite("opencv-threshold-example.jpg", dst);

#cv2.imshow('Original', image)
cv2.imshow('Umbralizar',dst)
#cv2.imshow('Kernel Blur', img)
#cv2.imshow('Gaussian', gaussian_blur)
#cv2.imshow('Median', median)
#cv2.imshow('Sharp', sharp_img)
#cv2.imshow('Bilateral', bilateral_filter)


cv2.waitKey()
cv2.imwrite('blur_kernel.jpg', img)
cv2.destroyAllWindows()