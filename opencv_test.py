import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# cap.set(3,480)
# cap.set(4,320)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# def rescale_frame(frame, percent=75):
#     width = int(frame.shape[1] * percent/ 100)
#     height = int(frame.shape[0] * percent/ 100)
#     dim = (width, height)
#     return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

# while True:
#     rect, frame = cap.read()
#     frame75 = rescale_frame(frame, percent=75)
#     cv2.imshow('frame75', frame75)
#     frame150 = rescale_frame(frame, percent=150)
#     cv2.imshow('frame150', frame150)