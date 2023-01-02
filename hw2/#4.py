import cv2
import numpy as np
import math

def isCircle(cont):
    length = cv2.arcLength(cont, True)
    area = cv2.contourArea(cont)
    if length:
        ratio = 4.* math.pi * area / (length * length)
        if ratio > 0.85:
            return True
    return False

def detect(file):
    # 이미지를 컬러로 읽r고 반전 처리
    src = ~cv2.imread(file, cv2.IMREAD_COLOR)
    # 이미지 읽기 예외처리
    if src is None:
        print('Image load failed!')
        exit()
    # 이미지를 그레이 스케일로 변환
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    # 노이즈 제거를 위한 블러 처리
    blurred = cv2.GaussianBlur(gray, (0, 0), 3)
    # 바이너리 이미지 만들기
    _, thr = cv2.threshold(blurred, 50, 255, cv2.THRESH_BINARY)

    # 모든 외곽선 검출
    contours, hier = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_L1)
    cv2.drawContours(src, contours, -1, (0, 255, 0), 2, cv2.LINE_8, hier)

    # 출력할 배열
    array = []
    hier = hier[0]
    
    for i, cont in enumerate(contours):
        if isCircle(cont):
            (x, y, w, h) = cv2.boundingRect(cont)
            array.append((x, y))

    n = len(array)
    visited = [False for _ in range(n)]
    dist = lambda a, b: ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5
    ans = []

    for i in range(n):
        if visited[i]: continue
        visited[i] = True
        cnt = 1
        for j in range(n):
            if visited[j] or i == j: continue
            if dist(array[i], array[j]) < 100:
                visited[j] = True
                cnt += 1
        ans.append(cnt)
    
    ans.sort()
    print(*ans, sep=' ')

    cv2.imshow('img', src)
    cv2.imshow('blur', blurred)
    cv2.imshow('thr', thr)
    cv2.waitKey()
    cv2.destroyAllWindows()

detect('img4_3.png')