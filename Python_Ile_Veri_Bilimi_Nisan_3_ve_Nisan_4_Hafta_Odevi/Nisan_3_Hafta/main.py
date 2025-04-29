import cv2
from ImageLoader import ImageLoader
from ColorChannelHandler import ColorChannelHandler

def main():

    image_path = "D:\\AcunMedya\\AcunMedya\\Python_Ile_Veri_Bilimi_Nisan_3_ve_Nisan_4_Hafta_Odevi\\Nisan_3_Hafta\\foto1.png"
    loader = ImageLoader(image_path)
    image = loader.load_image()
    loader.get_image()

    #Renk işleme için handler oluştur
    color_handler = ColorChannelHandler(image)
    color_handler.split_channels()

    #Kanallara ayır ve göster
    color_handler.split_channels()
    color_handler.show_channel(0,window_name="Mavi Kanal") #B
    color_handler.show_channel(1,window_name="Yesil Kanal") #G
    color_handler.show_channel(2,window_name="Kirmizi Kanal") #R

    #Griye çevir
    gray = color_handler.convert_to_gray()
    cv2.imshow("Gri Tonlama",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #HSV'ye çevir
    hsv_image = color_handler.convert_to_hsv()
    cv2.imshow("HSV Formati",hsv_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    

















if __name__ == "__main__":
    main()




