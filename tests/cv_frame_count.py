import numpy as np
import cv2

cap = cv2.VideoCapture('christmas-lights-misc/light_it_up.mp4')
i = 0

while (cap.isOpened()):
    ret, frame = cap.read()
    i += 1
    print(i)

    # cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(i)
cap.release()
cv2.destroyAllWindows()
