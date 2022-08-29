from abc import ABC, abstractmethod

import cv2
import PoseModule as pm


class exercise(ABC):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.detector = pm.poseDetector()
        self.count = 0
        self.direction = 0
        self.form = 0
        self.feedback = "Fix Form"

    def __del__(self):
        self.cap.release()

    @abstractmethod
    def start_exercise(self):
        pass
