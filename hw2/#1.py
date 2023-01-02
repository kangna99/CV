import cv2

def hough_circles(file):
    src = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        exit()
    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
    blurred = cv2.blur(src, (3, 3))
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 50, param1=150, param2=30)

    if circles is not None:
        for i in range(circles.shape[1]):
            cx, cy, radius = circles[0][i]
            cv2.circle(dst, (int(cx), int(cy)), int(radius), (0, 0, 255), 2, cv2.LINE_AA)
        print(circles.shape[1])

    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

hough_circles('1.png')
hough_circles('5.png')
hough_circles('7.png')
hough_circles('9.png')