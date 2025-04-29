import os
import cv2
import numpy as np


class ColorChannelHandler:
    def __init__(self,image):
        self.image = image
        self.channels = None

    #Görüntüyü mavi yeşil ve kırmızı kanallarına ayıracak.(BGR)
    def split_channels(self):
        self.channels = cv2.split(self.image)
        return self.channels

    #Hangi kanalı istersen onu ekranda görürsün.
    def show_channel(self,channel_index,window_name = "Kanal"):
        if self.channels is None:
            self.split_channels()
        cv2.imshow(window_name,self.channels[channel_index])
        cv2.waitKey(0)
        cv2.destroyAllWindows()   

    def convert_to_gray(self,save_path = None):
        gray_image = cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)

        if save_path is None:
            current_directory = os.getcwd()
            save_path = os.path.join(current_directory, "gray_image.jpg")

        cv2.imwrite(save_path,gray_image)
        return gray_image
        #Resmi griye çevirmemizin sebebi;
        #Bazen renkle ilgilenmiyoruz. Sadece şekil, parlaklık, kenar görmek istiyoruz.
        #Gri görüntü daha az veri taşır → işlem daha hızlı olur.
        #Yüz tanıma, kenar bulma gibi işler için gri yeterli olur.

    def convert_to_hsv(self): #Hue, Saturation, Value -> Renk, doygunluk(canlılık), parlaklık
        hsv_image = cv2.cvtColor(self.image,cv2.COLOR_BGR2HSV)
        return hsv_image
        ##HSV renk uzayı, renkleri daha iyi ayırt etmemizi sağlar.


        