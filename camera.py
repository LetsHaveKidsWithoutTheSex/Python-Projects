# camera

import cv2
import time

# 1. Create an object. Zero for external camera
video = cv2.VideoCapture(0)

a = 0
while True:
    a = a + 1
    check, frame = video.read()
    print(check)
    print(frame)  # representing image
    cv2.imshow('Capturing', frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
print(a)
video.release()

cv2.destroyAllWindows()




# button for terminating program
# button for 