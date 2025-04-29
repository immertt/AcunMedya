import cv2

class CameraHandler:
    def __init__(self,camera_index=0):
        self.camera_index = camera_index
        self.capture = None

    def start_camera(self):
        self.capture = cv2.VideoCapture(self.camera_index)
        if not self.capture.isOpened():
            raise ValueError("Kamera açılamadı.")
    #cv2.VideoCapture(0) → 0, bilgisayarın bağlı olduğu ilk kamerayı temsil eder. 
    #Birden fazla kamera varsa 1, 2 gibi değerler de kullanılabilir.

    def read_frame(self):
        if self.capture is None:
            raise ValueError("Kamera açılmadı, önce kamerayı başlatmalısınız.")
        ret,frame = self.capture.read()
        if not ret: #ret → başarı kontrolü True dönerse okuma başarılı demektir.
            raise ValueError("Kare okunamadı.")
        return frame

    def release_camera(self):
        if self.capture is not None:
            self.capture.release()
            self.capture = None #Kamera kapatıldığında capture nesnesini None yapıyoruz ki tekrar açılabilsin.
        cv2.destroyAllWindows()