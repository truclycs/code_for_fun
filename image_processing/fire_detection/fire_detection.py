import cv2
import numpy as np

# import argparse

# class Cam:
#     def __init__(self, background):
#         self.background = background

#     class __call__(self):pass

#     def backgroundSubtraction(self): pass

#     def filter(self): pass

video = cv2.VideoCapture("video1.mp4")


while True:
    grabbed, frame = video.read()
    if not grabbed:
        break

    blur = cv2.GaussianBlur(frame, (21, 21), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    lower = [18, 50, 50]
    upper = [35, 255, 255]
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")
    mask = cv2.inRange(hsv, lower, upper)

    output = cv2.bitwise_and(frame, hsv, mask=mask)
    no_red = cv2.countNonZero(mask)

    cv2.imshow("output", output)
    cv2.imshow("zzz", frame)
    print("output:", frame)
    if int(no_red) > 20000:
        print('Fire detected')
    print(int(no_red))
    print("output: {}".format(mask))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
video.release()
