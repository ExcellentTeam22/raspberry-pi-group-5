import cv2
import mediapipe as mp
import numpy as np
import PoseModule as pm
from exercise import exercise

# cap = cv2.VideoCapture (0)
# detector = pm.poseDetector ()
mp_pose = mp.solutions.pose


# count = 0
# direction = 0
# form = 0
# feedback = "Fix Form"

class squat(exercise):
    def start_exercise(self):
        ret, img = self.cap.read()  # 640 x 480
        # Determine dimensions of video - Help with creation of box in Line 43
        width = self.cap.get(3)  # float `width`
        height = self.cap.get(4)  # float `height`
        # print(width, height)

        img = self.detector.findPose(img, False)
        lmList = self.detector.findPosition(img, False)
        # print(lmList)
        if len(lmList) != 0:

            left_knee = self.detector.findAngle(img, mp_pose.PoseLandmark.LEFT_HIP.value,
                                                mp_pose.PoseLandmark.LEFT_KNEE.value,
                                                mp_pose.PoseLandmark.LEFT_ANKLE)
            right_knee = self.detector.findAngle(img, mp_pose.PoseLandmark.RIGHT_HIP.value,
                                                 mp_pose.PoseLandmark.RIGHT_KNEE.value,
                                                 mp_pose.PoseLandmark.RIGHT_ANKLE)
            hip = self.detector.findAngle(img, 11, 23, 25)

            # Percentage of success of pushup
            # per = np.interp (elbow, (90, 160), (0, 100))

            # Bar to show Pushup progress
            # bar = np.interp (elbow, (90, 160), (380, 50))

            # Check to ensure right form before starting the program
            if hip > 170 and left_knee > 160 and right_knee > 160:
                form = 1

            # Check for full range of motion for the pushup
            if form == 1:
                # if per == 0:
                if left_knee <= 80 and right_knee <= 80 and hip <= 75:
                    self.feedback = "Up"
                    if self.direction == 0:
                        self.count += 0.5
                        self.direction = 1
                else:
                    self.feedback = "Fix Form"

                # if per == 100:
                if left_knee > 160 and right_knee > 160 and hip > 160:
                    self.feedback = "Down"
                    if self.direction == 1:
                        self.count += 0.5
                        self.direction = 0
                else:
                    self.feedback = "Fix Form"
                    # form = 0

            print(self.count)

            # Draw Bar
            if form == 1:
                cv2.rectangle(img, (580, 50), (600, 380), (0, 255, 0), 3)
                # cv2.rectangle (img, (580, int (bar)), (600, 380), (0, 255, 0), cv2.FILLED)
                # cv2.putText (img, f'{int (per)}%', (565, 430), cv2.FONT_HERSHEY_PLAIN, 2,
                #             (255, 0, 0), 2)

            # Pushup counter
            cv2.rectangle(img, (0, 380), (100, 480), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, str(self.count), (25, 455), cv2.FONT_HERSHEY_PLAIN, 5,
                        (255, 0, 0), 5)

            # Feedback
            cv2.rectangle(img, (500, 0), (640, 40), (255, 255, 255), cv2.FILLED)
            cv2.putText(img, self.feedback, (500, 40), cv2.FONT_HERSHEY_PLAIN, 2,
                        (0, 255, 0), 2)

            ret, jpeg = cv2.imencode('.jpg', img)
            return jpeg.tobytes()
