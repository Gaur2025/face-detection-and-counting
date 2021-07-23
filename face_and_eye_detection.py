import numpy as np
import cv2

# We point OpenCV's Cascade classifier function to where our classifier (XML file format) is stored.
face_classifier = cv2.CascadeClassifier(
    'Haarcascades/haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')

# Loading the image then converting it to grayscale.
image = cv2.imread('image_examples/trump.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convering image to grayscale.

# Our classifier returns the ROI of the detected face as tuple.
# It stores the top left coordinate and the bottom right coordinates.
# detectMultiScale detects face in the image.
faces = face_classifier.detectMultiScale(gray, 1.3, 5)

# When no face is detected. face_classifier returns an empty tuple.
if faces is ():
    print(f"No faces found.")

    # We iterate through our faces array and draw a rectangle over each face in faces.
for (x, y, w, h) in faces:  # x = x-coordinate, y = y-coordinate, w = width of face, h = height of face
    # Drawing a rectangle on the face.
    cv2.rectangle(image, (x, y), (x + w, y + h), (127, 0, 255), 2)
    cv2.imshow("Face Detection", image)
    cv2.waitKey(0)
    # Now to detect the eyes, we need to crop the face.
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    # Detecting eyes in the cropped area.
    eyes = eye_classifier.detectMultiScale(roi_gray)
    # Drawing rectangles on the eyes.
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey),
                      (ex + ew, ey + eh), (255, 255, 0), 2)
        cv2.imshow('img', image)
        cv2.waitKey()

# This is very necessary, otherwise system would hang.
cv2.destroyAllWindows()
