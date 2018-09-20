# selfie01

import cv2
import dlib

video_capture = cv2.VideoCapture(0)

def trace_human_face(image):
    return image

while True:
    ret,frame = video_capture.read()
    scale = 0.5
    thumb = cv2.resize(frame, None, fx = scale, fy = scale,interpolation = cv2.INTER_AREA)
    gray = cv2.cvtColor(thumb , cv2.COLOR_BGR2GRAY)

    trace_huan_face(gray)
    cv2.imshow('Example',gray)

    if cv2.waitKey(1)  & 0xff  == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

# hello-word
