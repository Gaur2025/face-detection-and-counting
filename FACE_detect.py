import cv2

# Just base function for detectiong the face and counting.
# We point OpenCV's Cascade classifier function to where our classifier (XML file format) is stored.

faceCascade = cv2.CascadeClassifier(
    'Haarcascades/haarcascade_frontalface_default.xml')


def face_detect(image):
    i = 0
    # Loading the image then converting it to grayscale.
    img = cv2.imread(image)
    # Convering image to grayscale.
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ''' Our classifier returns the ROI of the detected face as tuple.
        It stores the top left coordinate and the bottom right coordinates.
    '''
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    # When no face is detected. face_classifier returns an empty tuple.
    # if faces is ():
    #     print(f"No faces found.")

    print(faces)
    print("Found {0} faces!".format(len(faces)))
    # We iterate through our faces array and draw a rectangle over each face in faces.
    for (x, y, w, h) in faces:  # x = x-coordinate, y = y-coordinate, w = width of face, h = height of face
        i = i+1
        # Drawing a rectangle on the face.
        cv2.rectangle(img, (x, y), (x + w, y + h), (95, 207, 30), 3)
        cv2.rectangle(img, (x, y - 40), (x + w, y), (95, 207, 30), -1)
        cv2.putText(img, 'F-'+str(i), (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
    cv2.imshow("Faces found", img)
    cv2.waitKey(0)


face_detect('image_examples/Trump.jpg')
# This is very necessary, otherwise system would hang.
cv2.destroyAllWindows()
