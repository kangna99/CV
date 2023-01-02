import cv2

# 원 검출
def hough_circles(x, y, w, h):
    rect = blurred[y: y+h, x: x+w]
    tmp = dst[y:y+h, x:x+w]
    circles = cv2.HoughCircles(rect, cv2.HOUGH_GRADIENT, 1, 35, param1=250, param2=40)

    if circles is not None:
        for i in range(circles.shape[1]):
            cx, cy, radius = circles[0][i]
            cv2.circle(tmp, (int(cx), int(cy)), int(radius), (0, 0, 255), 2, cv2.LINE_AA)
        array.append(circles.shape[1])
        # cv2.imshow('rect', rect); cv2.waitKey()
        # cv2.destroyAllWindows()

def detect():
    # 바이너리 이미지 만들기
    ret, thr = cv2.threshold(blurred, 0, 255, cv2.THRESH_OTSU)
    # 바깥 외곽선만 검출하여 리스트로 묶어줌(사각형 검출)
    contours, _ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cont in contours:
        # 외곽선 근사화
        # contour가 그리는 길이에 2% 오차를 둠
        approx = cv2.approxPolyDP(cont, cv2.arcLength(cont, True) * 0.02, True)
        # 외곽의 꼭짓점의 수를 구해 vtc에 저장
        vtc = len(approx)
        if vtc == 4:
            (x, y, w, h) = cv2.boundingRect(cont)
            pt1 = (x, y)
            pt2 = (x + w, y + h)
            cv2.rectangle(dst, pt1, pt2, (255, 0, 0), 2)
            hough_circles(x, y, w, h)

# 파일을 입력 받음
file = input()
# 이미지를 그레이 스케일로 읽기
src = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
# 이미지 읽기 예외처리
if src is None:
    print('Image load failed!')
    exit()
# 허프 변환 함수가 노이즈에 민감하므로 블러링하여 노이즈 제거
blurred = cv2.GaussianBlur(src, (0, 0), 1)
# 출력할 이미지 dst
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

# 출력할 배열
array = []
# 검출(사각형을 우선적으로 검출한 후 각 사각형에 대하여 원 검출)
detect()
# 오름차순으로 배열 정렬 후 출력
array.sort()
print(array)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()