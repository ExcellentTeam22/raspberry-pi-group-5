import cv2
import mediapipe as mp
import numpy as np
import PoseModule as pm
from datetime import datetime
#from get_angles import *

cap = cv2.VideoCapture (0)
detector = pm.poseDetector ()
mp_pose = mp.solutions.pose
count = 0
direction = 1
form = 0
feedback = "Fix Form"
counter = 0

while cap.isOpened ():
    ret, img = cap.read()  # 640 x 480
    # Determine dimensions of video - Help with creation of box in Line 43
    width = cap.get (3)  # float `width`
    height = cap.get (4)  # float `height`
    # print(width, height)

    img = detector.findPose (img, False)
    lmList = detector.findPosition (img, False)
    # print(lmList)
    if len (lmList) != 0:
        form = 0
        left_elbow = detector.findAngle(img, mp_pose.PoseLandmark.LEFT_SHOULDER, mp_pose.PoseLandmark.LEFT_ELBOW,
                              mp_pose.PoseLandmark.LEFT_WRIST)
        right_elbow = detector.findAngle(img, mp_pose.PoseLandmark.RIGHT_SHOULDER, mp_pose.PoseLandmark.RIGHT_ELBOW,
                              mp_pose.PoseLandmark.RIGHT_WRIST)
        hip = detector.findAngle (img, 11, 23, 25)

        right_shoulder = detector.findAngle(img,14,12,24)

        left_shoulder = detector.findAngle(img,13,11,23)

        # Percentage of success of pushup
        #per = np.interp (elbow, (90, 160), (0, 100))

        # Bar to show Pushup progress
        #bar = np.interp (elbow, (90, 160), (380, 50))

        # Check to ensure right form before starting the program
        start = datetime.now().time()

        # Check for full range of motion for the pushup
        if direction == 0:# up form
            if counter % 10 == 0:
                feedback = "Up"
            # if per == 0:
            if 90 < hip < 160 and 150 < left_elbow < 190 and 20 < left_shoulder < 70:
                feedback = "Up"
                if direction == 0:
                    count += 0.5
                    direction = 1
            else:
                end = datetime.now().time()
                if counter % 30 == 0:
                    counter = 1
                    # print("s: ", start)
                    # print("e: ", end)
                    # print("e-s : ", end.second - start.second)

                    if not 150 < left_elbow < 180:
                        print(1)
                        feedback = "150 < elbow < 180"
                    elif not 90 < hip < 160:
                        print(2)
                        feedback = "90 < hip < 160"
                    elif not 20 < left_shoulder < 50:
                        print(3)
                        feedback = "20 < shoulder < 50"
                    else:
                        print(4)
                        feedback = "Fix Form"

            #if per == 100:
        if direction == 1: # down form
            if counter % 10 == 0:
                feedback = "Down"
            if 90 < hip < 160 and 80 < left_elbow < 110 and 80 < left_shoulder < 110:

                feedback = "Down"
                if direction == 1:
                    count += 0.5
                    direction = 0

            else:
                if counter % 30 == 0:
                    counter = 1
                end = datetime.now().time()

                # print("s: ", start)
                # print("e: ", end)
                # print("e-s : ", end.second - start.second)

                if not 80 < left_elbow < 110:
                    print(5)
                    feedback = "80 < left_elbow < 110"
                elif not 100 < hip < 160:
                    print(6)
                    feedback = "100 < hip < 160"
                elif not 80 < left_shoulder < 110:
                    print(7)
                    feedback = "80 < left_shoulder < 110"
                else:
                    print(8)
                    feedback = "Fix Form"
                # form = 0

        # print (count)

        # Draw Bar
        if form == 1:
            cv2.rectangle (img, (580, 50), (600, 380), (0, 255, 0), 3)
            #cv2.rectangle (img, (580, int (bar)), (600, 380), (0, 255, 0), cv2.FILLED)
            #cv2.putText (img, f'{int (per)}%', (565, 430), cv2.FONT_HERSHEY_PLAIN, 2,
            #             (255, 0, 0), 2)

        # Pushup counter
        cv2.rectangle (img, (0, 380), (100, 480), (0, 255, 0), cv2.FILLED)
        cv2.putText (img, str (int (count)), (25, 455), cv2.FONT_HERSHEY_PLAIN, 5,
                     (255, 0, 0), 5)

        # Feedback
        cv2.rectangle (img, (500, 0), (640, 40), (255, 255, 255), cv2.FILLED)
        cv2.putText (img, feedback, (100, 40), cv2.FONT_HERSHEY_PLAIN, 2,
                     (0, 255, 0), 2)
        counter+=1


    cv2.imshow ('bench dips counter', img)
    if cv2.waitKey (10) & 0xFF == ord ('q'):
        break

cap.release ()
cv2.destroyAllWindows()
