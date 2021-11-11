import cv2
import numpy as np


video_file = "3.mp4"
video = cv2.VideoCapture(0)
i = 0
backSub = cv2.createBackgroundSubtractorKNN()


def back_sub(frame):
    frame_backsub = backSub.apply(frame)
    frame_backsub[frame_backsub < 255] = 0
    output = cv2.bitwise_and(frame, frame, mask=frame_backsub)
    return output


def filter_image(frame):
    blur = cv2.GaussianBlur(frame, (21, 21), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    # lower = [18, 50, 50]
    # upper = [35, 255, 255]

    lower = [18, 0, 0]
    upper = [35, 255, 255]

    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    mask = cv2.inRange(hsv, lower, upper)

    output = cv2.bitwise_and(frame, hsv, mask=mask)
    # output = cv2.bitwise_and(hsv, hsv, mask=mask)
    return output

# def back_sub1(frame):
#     frame_backsub = backSub.apply(frame)
#     # print(frame_backsub)
#     # frame_backsub[frame_backsub < 255] = 0
#     # print(frame_backsub)
#     return frame_backsub


while True:
    (grabbed, frame) = video.read()
    if not grabbed:
        break

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    frame_backsub = back_sub(frame)
    frame_filter = filter_image(frame)

    output = cv2.bitwise_and(frame_backsub, frame_filter)

    # frame_backsub1 = back_sub1(frame)

    # cv2.imshow('Frame_Sub', frame_backsub)
    # cv2.imshow('Frame_Sub1', frame_backsub1)

    cv2.imshow('Frame', frame)
    cv2.imshow('Output', output)

    keyboard = cv2.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break

# while True:
#     (grabbed, frame) = video.read()
#     if not grabbed:
#         break

#     frame_bgsub = back_sub(frame)
#     frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     contours = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

#     blur = cv2.GaussianBlur(frame, (21, 21), 0)
#     hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

#     # lower = [18, 50, 50]
#     # upper = [35, 255, 255]

#     lower = [18, 0, 0]
#     upper = [35, 255, 255]

#     lower = np.array(lower, dtype="uint8")
#     upper = np.array(upper, dtype="uint8")
#     mask = cv2.inRange(hsv, lower, upper)

#     # output = cv2.bitwise_and(frame, hsv, mask=mask)
#     output = cv2.bitwise_and(hsv, hsv, mask=mask)
#     no_red = cv2.countNonZero(mask)

#     cv2.imshow("output", output)
#     # print("output:", frame)

#     if int(no_red) > 20000:
#         print ('Fire detected ', i)
#         i += 1
#     else:
#         print('No fire')

#     #print(int(no_red))
#     #print("output:".format(mask))
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#     cv2.waitKey(10)

cv2.destroyAllWindows()
video.release()
