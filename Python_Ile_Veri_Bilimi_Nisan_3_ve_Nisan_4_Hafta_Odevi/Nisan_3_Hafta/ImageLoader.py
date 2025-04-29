import cv2

class ImageLoader:

    def __init__(self,image_path):
        self.image_path = image_path
        self.image = None

    def load_image(self):
        self.image = cv2.imread(self.image_path)
        if self.image is None:
            raise ValueError("Görüntü yüklenemedi, dosya yolunu kontrol ediniiz.")
        return self.image

    def get_image(self,window_name = "Goruntu"):
        if self.image is None:
            raise ValueError("Öncelikle görüntüyü yükleyin.")
        cv2.imshow(window_name,self.image)
        cv2.waitKey(0) #Herhangi bir tuşa basmazsan görünte kapanmaz. waitKey(5000) 5s bekler.
        cv2.destroyAllWindows() #Açık olan bütün OpenCV pencerelerini kapatır.



