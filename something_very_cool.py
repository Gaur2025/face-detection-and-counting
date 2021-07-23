###### Capture and mouse draw rectangle from webcam and sketch process it in a live feed. ######

import numpy as np
import cv2
import matplotlib.pyplot as plt


def sketch_transform(image):
    # Converting to grayscale image.
    image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_grayscale_blurred = cv2.GaussianBlur(image_grayscale, (7, 7), 0)
    # Canny function finds edges in the image.
    image_canny = cv2.Canny(image_grayscale_blurred, 10, 80)
    _, mask = image_canny_imverted = cv2.threshold(
        image_canny, 30, 255, cv2.THRESH_BINARY_INV)
    return mask


cam_capture = cv2.VideoCapture(0)
cv2.destroyAllWindows()

while True:
    _, im0 = cam_capture.read()
    showCrosshair = False
    fromCenter = False
    r = cv2.selectROI("Image", im0, fromCenter, showCrosshair)
    break

while True:
    _, image_frame = cam_capture.read()

    rect_img = image_frame[int(r[1]): int(
        r[1] + r[3]), int(r[0]): (r[0] + r[2])]

    sketcher_rect = rect_img
    sketcher_rect = sketch_transform(sketcher_rect)

    # Conversion for 3 channels to put back on original image (streaming)
    sketcher_rect_rgb = cv2.cvtColor(sketcher_rect, cv2.COLOR_GRAY2RGB)

    # Replacing the sketched image on region of interest.
    image_frame[int(r[1]): int(r[1] + r[3]), int(r[0])                : (r[0] + r[2])] = sketcher_rect_rgb

    cv2.imshow("Sketcher ROI", image_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):   # 1 => enter key.
        break

cam_capture.release()
cv2.destroyAllWindows()
