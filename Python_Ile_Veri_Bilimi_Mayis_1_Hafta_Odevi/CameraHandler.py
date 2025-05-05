import cv2

class CameraHandler():
    def __init__(self,camera_index=0):
        self.camera_index = camera_index
        self.capture = None 

    def start_camera(self):
        self.capture = cv2.VideoCapture(self.camera_index)
        if not self.capture.isOpened():
            raise ValueError("Kamera açılmadı")

    def read_frame(self):
        if not self.capture.isOpened():
            raise ValueError("Kamera açılmadı")
        
        ret,frame = self.capture.read()
        if not ret:
            raise ValueError("Kare bulunamadı")
        return frame


    def release_camera(self):
        if self.capture.isOpened():
            self.capture.release()
            self.capture = None  
        cv2.destroyAllWindows()