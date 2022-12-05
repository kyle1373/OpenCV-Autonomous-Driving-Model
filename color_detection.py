# TechVidvan Object detection of similar color

import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    # ret, frame = cap.read()
    img = cv2.imread('colortest1.jpg')

    imageToUse = img
    # convert to hsv colorspace
    hsv = cv2.cvtColor(imageToUse, cv2.COLOR_BGR2HSV)

    # lower bound and upper bound for blue color
    lower_blue = np.array([100, 0, 0])	 
    upper_blue = np.array([360, 50, 50])

    # find the colors within the boundaries
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # Showing the output

    result = cv2.bitwise_and(imageToUse, imageToUse, mask=mask)

    cv2.imshow("Image", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()