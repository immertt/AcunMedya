import cv2

class CameraHandler:
    
    def __init__(self,camera_index=0):
        self.camera_index = camera_index
        self.capture = None

    def start_camera(self):
        self.capture = cv2.VideoCapture(self.camera_index)
        if not self.capture.isOpened():
            raise RuntimeError("Kamera açılmadı")

    def read_frames(self):
        if not self.capture.isOpened():
            raise RuntimeError("Öncelikle start_camera metodunu çagırın")
        
        ret,frame = self.capture.read()
        if not ret:
            raise RuntimeError("Kare alınamadı")
        
        return frame

    def release_camera(self):
        if self.capture.isOpened():
            self.capture.release()
            self.capture = None
        cv2.destroyAllWindows()



