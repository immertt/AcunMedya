from CameraHandler import CameraHandler
from FingerCounter import FingerCounter
from HandDetector import HandDetector
from FrameDrawer import FrameDrawer
import cv2

def process_frame(frame, results, h_detector, f_counter, drawer):
    for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
        h_detector.draw_landmarks(frame, hand_landmarks)
        lm_list = h_detector.get_landmarks_list(frame, hand_landmarks)

        hand_label = results.multi_handedness[idx].classification[0].label
        hand_label = "Left" if hand_label == "Right" else "Right"

        if lm_list:
            fingers = f_counter.count_fingers(lm_list, hand_label)
            total_fingers = sum(fingers)

            command = ""
            if total_fingers == 1 and fingers[1] == 1 and all(f == 0 for i, f in enumerate(fingers) if i != 1):
                command = "Yukari"
            elif total_fingers == 5:
                command = "Dur"
            elif total_fingers == 0:
                command = "Hazir"
            else:
                command = f"{total_fingers} Parmak"

            drawer.draw_text(frame, f"{hand_label} Hand: {total_fingers} Fingers", position=(10, 70 + 80 * idx))
            drawer.draw_text(frame, f"Komut: {command}", position=(10, 70 + 80 * idx + 30))

class FingerApp:
    def __init__(self):
        self.camera = CameraHandler()
        self.f_counter = FingerCounter()
        self.h_detector = HandDetector()
        self.drawer = FrameDrawer()

    def run(self):
        self.camera.start_camera()
        print("Kamera açıldı, çıkış için 'q'ya basınız")
        running = True

        while running:
            frame = self.camera.read_frame()
            results = self.h_detector.detect_hands(frame)

            if results.multi_hand_landmarks:
                process_frame(frame, results, self.h_detector, self.f_counter, self.drawer)

            cv2.imshow("El ve Parmak Sayaci", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 27:
                running = False

        self.camera.release_camera()
        print("Kamera kapatıldı.")

def main():
    app = FingerApp()
    app.run()

if __name__ == "__main__":
    main()