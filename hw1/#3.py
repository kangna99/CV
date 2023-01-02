import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print('Camera open failed')
    exit()

w = round(cap.get(cv.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv.CAP_PROP_FPS)

fourcc = cv.VideoWriter_fourcc(*'DIVX')  # *'DIVX' == 'D', 'I', 'V', 'X'
delay = round(1000 / fps)

outputVideo = cv.VideoWriter('output.avi', fourcc, fps, (w, h), False)

if not outputVideo.isOpened():
    print('File open failed!')
    exit()

# print(fps)

prv = -1
flag = False
cnt = 0

while True:
    ret, frame = cap.read()
    if not ret: break
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cur = np.mean(frame)

    if prv != -1 and abs(cur - prv) > 30:
        # print(cur, prv, cnt)
        flag = True
    prv = cur

    if flag and cnt < fps * 3:
        frame = ~frame
        cnt += 1

    cv.imshow('frame', frame)
    outputVideo.write(frame)
    if cv.waitKey(delay) == 27: break

cv.destroyAllWindows()

