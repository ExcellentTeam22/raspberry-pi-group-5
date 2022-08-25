import PoseModule as pm
import mediapipe as mp

mp_pose = mp.solutions.pose

detector = pm.poseDetector()


def get_left_elbow(img):
    return detector.findAngle(img, mp_pose.PoseLandmark.LEFT_SHOULDER, mp_pose.PoseLandmark.LEFT_ELBOW,
                              mp_pose.PoseLandmark.LEFT_WRIST)


def get_right_elbow(img):
    return detector.findAngle(img, mp_pose.PoseLandmark.RIGHT_SHOULDER, mp_pose.PoseLandmark.RIGHT_ELBOW,
                              mp_pose.PoseLandmark.RIGHT_WRIST)


def get_left_hip(img):
    return detector.findAngle(img, mp_pose.PoseLandmark.LEFT_SHOULDER, mp_pose.PoseLandmark.LEFT_HIP,
                              mp_pose.PoseLandmark.LEFT_KNEE)


def get_right_hip(img):
    return detector.findAngle(img, mp_pose.PoseLandmark.RIGHT_SHOULDER, mp_pose.PoseLandmark.RIGHT_HIP,
                              mp_pose.PoseLandmark.RIGHT_KNEE)


def get_left_knee(img):
    return detector.findAngle(img, mp_pose.PoseLandmark.LEFT_HIP, mp_pose.PoseLandmark.LEFT_KNEE,
                              mp_pose.PoseLandmark.LEFT_ANKLE)


def get_right_knee(img):
    return detector.findAngle(img, mp_pose.PoseLandmark.RIGHT_HIP, mp_pose.PoseLandmark.RIGHT_KNEE,
                              mp_pose.PoseLandmark.RIGHT_ANKLE)
