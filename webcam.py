import numpy as np #pip install numpy
import cv2 #pip install opencv-python

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
