# TechVidvan Object detection of similar color

import cv2
import numpy as np

class image_functions():

    def getSteeringAndThrottleFromImage(image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # lower bound and upper bound for blue color
        lower_blue = np.array([97, 26, 0])	 
        upper_blue = np.array([255, 255, 160])

        # lower bound and upper bound for blue color
        lower_green = np.array([50, 45, 52])	 #[50, 12, 52]
        upper_green = np.array([100, 160, 222])   #[100, 71, 222]

        # find the colors within the boundaries
        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
        mask_green = cv2.inRange(hsv, lower_green, upper_green)

        # filter noise
        #define kernel size  
        kernel = np.ones((7,7),np.uint8)

        # Remove unnecessary noise from mask

        mask_blue = cv2.morphologyEx(mask_blue, cv2.MORPH_CLOSE, kernel)
        mask_blue = cv2.morphologyEx(mask_blue, cv2.MORPH_OPEN, kernel)

        mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_CLOSE, kernel)
        mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_OPEN, kernel)

        # Showing the output

        resultblue = cv2.bitwise_and(image, image, mask=mask_blue)
        resultgreen = cv2.bitwise_and(image, image, mask=mask_green)

        bluepixels = np.sum(resultblue != 0)
        greenpixels = np.sum(resultgreen != 0)

        # print("{} and {}".format("bluepixels is ", bluepixels))
        # print("{} and {}".format("greenpixels is ", greenpixels))

        turnresult = greenpixels - bluepixels

        throttle = 40

        if(turnresult < 0):
            # left
            steering = -.5
        else:
            # right
            steering = .5
        
        return steering, throttle
        
