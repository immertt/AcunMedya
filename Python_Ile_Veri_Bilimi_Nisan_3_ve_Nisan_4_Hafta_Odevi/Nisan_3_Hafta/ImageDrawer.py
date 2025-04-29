import cv2

class ImageDrawer:
    def __init__(self,image):
        self.image = image

    def put_text(self,text,position,font_scale=1,color=(0,255,255),thickness=3):
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(self.image,text,position,font,font_scale,color,thickness)    