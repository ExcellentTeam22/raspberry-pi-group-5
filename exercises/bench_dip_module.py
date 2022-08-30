from datetime import datetime

import cv2

from exercises.exercise import exercise

import mediapipe as mp
mp_pose = mp.solutions.pose
class benchDips(exercise):
    def __init__(self):
        super().__init__()
        self.counter = 0

    def start_exercise(self):
        ret, img = self.cap.read()  # 640 x 480
        # Determine dimensions of video - Help with creation of box in Line 43
        width = self.cap.get (3)  # float `width`
        height = self.cap.get (4)  # float `height`
        # print(width, height)

        img = self.detector.findPose (img, False)
        lmList = self.detector.findPosition (img, False)
        # print(lmList)
        if len (lmList) != 0:
            form = 0
            left_elbow = self.detector.findAngle(img, mp_pose.PoseLandmark.LEFT_SHOULDER, mp_pose.PoseLandmark.LEFT_ELBOW,
                                  mp_pose.PoseLandmark.LEFT_WRIST)
            right_elbow = self.detector.findAngle(img, mp_pose.PoseLandmark.RIGHT_SHOULDER, mp_pose.PoseLandmark.RIGHT_ELBOW,
                                  mp_pose.PoseLandmark.RIGHT_WRIST)
            hip = self.detector.findAngle (img, 11, 23, 25)

            right_shoulder = self.detector.findAngle(img,14,12,24)

            left_shoulder = self.detector.findAngle(img,13,11,23)

            # Percentage of success of pushup
            #per = np.interp (elbow, (90, 160), (0, 100))

            # Bar to show Pushup progress
            #bar = np.interp (elbow, (90, 160), (380, 50))

            # Check to ensure right form before starting the program
            start = datetime.now().time()

            # Check for full range of motion for the pushup
            if self.direction == 0:# up form
                if self.counter % 10 == 0:
                    self.feedback = "Up"
                # if per == 0:
                if 90 < hip < 160 and 150 < left_elbow < 190 and 20 < left_shoulder < 70:
                    feedback = "Up"
                    if self.direction == 0:
                        self.count += 0.5
                        self.direction = 1
                else:
                    end = datetime.now().time()
                    if self.counter % 30 == 0:
                        self.counter = 1
                        # print("s: ", start)
                        # print("e: ", end)
                        # print("e-s : ", end.second - start.second)

                        if not 150 < left_elbow < 180:
                            print(1)
                            self.feedback = "150 < elbow < 180"
                        elif not 90 < hip < 160:
                            print(2)
                            self.feedback = "90 < hip < 160"
                        elif not 20 < left_shoulder < 50:
                            print(3)
                            self.feedback = "20 < shoulder < 50"
                        else:
                            print(4)
                            self.feedback = "Fix Form"

                #if per == 100:
            if self.direction == 1: # down form
                if self.counter % 10 == 0:
                    self.feedback = "Down"
                if 90 < hip < 160 and 80 < left_elbow < 110 and 80 < left_shoulder < 110:

                    self.feedback = "Down"
                    if self.direction == 1:
                        self.count += 0.5
                        self.direction = 0

                else:
                    if self.counter % 30 == 0:
                        self.counter = 1
                    end = datetime.now().time()

                    # print("s: ", start)
                    # print("e: ", end)
                    # print("e-s : ", end.second - start.second)

                    if not 80 < left_elbow < 110:
                        print(5)
                        self.feedback = "80 < left_elbow < 110"
                    elif not 100 < hip < 160:
                        print(6)
                        self.feedback = "100 < hip < 160"
                    elif not 80 < left_shoulder < 110:
                        print(7)
                        self.feedback = "80 < left_shoulder < 110"
                    else:
                        print(8)
                        self.feedback = "Fix Form"
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
            cv2.putText (img, str (self.count), (25, 455), cv2.FONT_HERSHEY_PLAIN, 5,
                         (255, 0, 0), 5)

            # Feedback
            cv2.rectangle (img, (500, 0), (640, 40), (255, 255, 255), cv2.FILLED)
            cv2.putText (img, self.feedback, (100, 40), cv2.FONT_HERSHEY_PLAIN, 2,
                         (0, 255, 0), 2)
            self.counter+=1

        ret, jpeg = cv2.imencode('.jpg', img)
        return jpeg.tobytes()