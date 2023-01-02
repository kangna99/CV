import numpy as np
import cv2 as cv

def saturated(value):
    if value > 255:
        value = 255
    elif value < 0:
        value = 0

    return value


src = cv.imread('sample.jpg', cv.IMREAD_GRAYSCALE)
mean = np.mean(src, dtype=np.int32)

if src is None:
    print('Image load failed!')
    exit()

alpha = 2.0
dst = np.empty(src.shape, src.dtype)
for y in range(src.shape[0]):
    for x in range(src.shape[1]):
        dst[y, x] = saturated(src[y, x] + (src[y, x] - mean) * alpha)
# cv.imshow('src', src)
# cv.imshow('dst', dst)
# cv.waitKey()
cv.imwrite('contrast.jpg', dst)
