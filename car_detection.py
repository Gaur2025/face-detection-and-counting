import numpy as np
import cv2
import time

# Creating body classifier
car_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_car.xml')

# Initialize video capture for the video file.
# Add any video conatinaing cars and save it into /image_examples directory. Then use next line of code for car detection.
cap = cv2.VideoCapture('image_examples/cars.avi')

# Loop once video is loaded.
while cap.isOpened():
    time.sleep(0.05)  # To slow the video.
    # Reading first frame.
    ret, frame = cap.read()
    #frame = cv2.resize(frame, None, fx = 0.5, fy = 0.5, interpolating = cv2.INTER_LINEAR)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Passing frame to body classifier.
    cars = car_classifier.detectMultiScale(gray, 1.4, 2)

    # Extracting bounding boxes for any bodies identified.
    for (x, y, w, h) in cars:
        # Drawing a rectangle on the face.
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.imshow('Cars', frame)

    if cv2.waitKey(1) == 13:  # 13 is the enter key.
        break

cap.release()
cv2.destroyAllWindows()
