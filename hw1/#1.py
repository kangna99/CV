import numpy as np
import cv2 as cv

src = cv.imread('sample.jpg', cv.IMREAD_GRAYSCALE)
mean = np.mean(src, dtype=np.int32)

if src is None:
    print('Image load failed!')
    exit()

dst = np.empty(src.shape, src.dtype)
for y in range(src.shape[0]):
    for x in range(src.shape[1]):
        if src[y, x] < mean:
            dst[y, x] = 0
        else:
            dst[y, x] = src[y, x]
# cv.imshow('src', src)
# cv.imshow('dst', dst)
# cv.waitKey()
# cv.destroyAllWindows()
cv.imwrite('output.jpg', dst)