import numpy as np
import cv2

# We point OpenCV's Cascade classifier function to where our classifier (XML file format) is stored.
face_cascade = cv2.CascadeClassifier(
    'Haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')

# Defining a function that would do the detections.


def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        # Drawing a rectangle on the face.
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # Now to detect the eyes, we need to crop the face.
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        # Detecting eyes in the cropped area.
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    return frame


# Doing face recognition with the webcam.
video_capture = cv2.VideoCapture(0)   # 0 => used to use default webcam.
while True:     # To get continuous frames.
    _, frame = video_capture.read()   # frames are captured.
    # Converting above frames into Grayscale coz RGM frames take lot of time to process.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)   # Detect function is defined above.
    cv2.imshow('Video', canvas)
    # Unless user presses 'enter' or 'q'; it would not brake.
    if cv2.waitKey(13) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()  # press 'q' to quit.
