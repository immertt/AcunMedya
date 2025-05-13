from CameraHandler import CameraHandler
from FaceMeshDetector import FaceMeshDetector
from EyeTracker import EyeTracker
import cv2

def main():
    camera = CameraHandler()
    face_mesh = FaceMeshDetector(max_faces=1)
    eye_tracker = EyeTracker()

    camera.start_camera()
    running = True

    while running:
        frame = camera.read_frames()
        h,w,_ = frame.shape

        results = face_mesh.detect_faces(frame) 

        if results.multi_face_landmarks:
            for face_landmark in results.multi_face_landmarks:
                face_mesh.draw_landmarks(frame,face_landmark)

                left_iris = eye_tracker.iris_center(face_landmark.landmark,eye_tracker.LEFT_IRIS,w,h)
                right_iris = eye_tracker.iris_center(face_landmark.landmark,eye_tracker.RIGHT_IRIS,w,h)

                cv2.circle(frame, left_iris, 3, (255, 0, 0), -1) #gözün sol iris merkezi
                cv2.circle(frame, right_iris, 3, (255, 0, 0), -1) #gözün sag iris merkezi

                direction = eye_tracker.analyze_eye(left_iris, right_iris, w) #bakış yönü

                cv2.putText(frame, f"Direction: {direction}", (30, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Eye Tracking", frame)

        key = cv2.waitKey(1) & 0xFF
        if key in [27, ord('q')]:
            running = False

    camera.release_camera()
    print("Kamera kapatıldı.")

if __name__ == "__main__":
    main()



