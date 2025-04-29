from CameraHandler import CameraHandler
from FaceAnalyzer import FaceAnalyzer
from SmileDetector import SmileDetector
from FrameDrawer import FrameDrawer
import cv2

def main():
    camera = CameraHandler()
    analyzer = FaceAnalyzer()
    detector = SmileDetector()
    drawer = FrameDrawer()

    try:
        camera.start_camera()
        print("Kamera başlatıldı, çıkmak için q harfine basınız.")

        while True:
            frame = camera.read_frame() #frame'i kareleri okuyoruz
            frame = cv2.flip(frame, 1)
            faces = analyzer.detect_faces(frame=frame) #yüzleri tespit ediyoruz.

            for (x,y,w,h) in faces:
                face_crop = frame[y:y+h,x:x+w]

                results = analyzer.analyze_faces(face_crop)
                if results:
                    face_data = results[0]
                    is_smiling = detector.is_smiling(face_data)

                    if is_smiling: #gülümsüyorsa
                        drawer.draw_labelled_box(frame, x, y, w, h, label="Happyy")

            cv2.imshow("Gülümseme Tespiti", frame)

            # 'q' tuşu ile çık
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        print("Hata:",e)

    finally:
        camera.release_camera()        

if __name__ == "__main__":
    main()
