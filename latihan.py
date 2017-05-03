import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    negatif = (255 - gray)
    
    brightness = (frame + 25)

    # Display the resulting frame
    cv2.imshow('Gambar Asli',frame)
    cv2.imshow('Mengganti Brightness',brightness)
    cv2.imshow('frame',gray)
    cv2.imshow('invert',negatif)
    if cv2.waitKey(1) & 0xFF == ord('w'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()