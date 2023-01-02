import numpy as np
import cv2
import math

def isCircle(cont):
    length = cv2.arcLength(cont, True)
    area = cv2.contourArea(cont)
    if length:
        ratio = 4 * math.pi * area / (length * length)

        if ratio > 0.85:
            return True
            # setLabel(src, cont, 'CIR')
    return False

def detect(file):
    # 이미지를 컬러로 읽기
    src = cv2.imread(file, cv2.IMREAD_COLOR)
    # 이미지 읽기 예외처리
    if src is None:
        print('Image load failed!')
        exit()
    # 이미지를 그레이 스케일로 변환
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    # 노이즈 제거를 위한 블러 처리
    blurred = cv2.GaussianBlur(gray, (0, 0), 3)
    # 바이너리 이미지 만들기
    _, thr = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)


    # 모든 외곽선 검출
    contours, hier = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_L1)
    cv2.drawContours(src, contours, -1, (0, 255, 0), 2, cv2.LINE_8, hier)
    hier = hier[0]

    # 출력할 배열
    array = []
    for _ in range(len(hier)):
        array.append(0)

    # 부모가 있는 외곽선은 원인지 검사하고 count 증가
    for i, cont in enumerate(contours):
        parent = hier[i][3]
        if parent != -1 and isCircle(cont):
            array[parent] += 1

    # 오름차순으로 배열 정렬 후 출력
    array = sorted([x for x in array if x != 0])
    print(array)

    cv2.imshow('src', src)
    cv2.imshow('thr', thr)
    cv2.waitKey()
    cv2.destroyAllWindows()

detect('img3_1.png')
detect('img3_2.png')
detect('img3_3.png')
detect('img3_4.png')