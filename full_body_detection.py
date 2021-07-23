import numpy as np
import cv2

# Creating body classifier
body_classifier = cv2.CascadeClassifier(
    'Haarcascades/haarcascade_fullbody.xml')

# Initialize video capture for the video file.
cap = cv2.VideoCapture('image_examples/walking.avi')

# Loop once video is loaded.
while cap.isOpened():
    # Reading first frame.
    ret, frame = cap.read()
    #frame = cv2.resize(frame, None, fx = 0.5, fy = 0.5, interpolating = cv2.INTER_LINEAR)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Passing frame to body classifier.
    bodies = body_classifier.detectMultiScale(gray, 1.2, 3)

    # Extracting bounding boxes for any bodies identified.
    for (x, y, w, h) in bodies:
        # Drawing a rectangle on the face.
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.imshow('Pedestrians', frame)

    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()
