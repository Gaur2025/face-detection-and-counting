# This Repository contains programs to detect objects using OpenCV.
# Haarcascades XML files are used to create claasifiers. All xml files are stored in */Haarcascades* directory.
# Some image and video examples are saved in */image_examples* directory for testing purposes.

1. app.py 
    - This file contains face detection and counting code.
    - It is also deployed(Very basic version) using streamlit.
    - User can upload any image and detect faces. Results can also be downloaded in image format.

2. car_detection.py
    - Detects cars in a video.
    - Rectangles are created around the video.

3. face_and_eye_detection.py
    - Detects face as well as eyes from a picture.
    - It can be also modified for live videos from webcam or any other camera source.

4. face_and_eye_detection_using_webcam.py
    - Detects live faces and eyes from a live webcam.

5. full_body_detection.py
    - Detects full body from a video source file.
    - It can be used as pedestrian detection tool or modified to some social distancing verifier.

6. something_very_cool.py
    - This program lets user to draw a rectangle on the first frame captured by webcam.
    - Then this frame remains in sketch format.
    - It looks really cool...just try it out.

## NOTE:- To close/quit cv2 frames press- Enter or 'q'.