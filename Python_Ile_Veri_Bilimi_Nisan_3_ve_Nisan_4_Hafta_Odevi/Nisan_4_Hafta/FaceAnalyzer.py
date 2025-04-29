#Kameradan aldığımız her frame üzerinde DeepFace kullanarak yüzleri bulacak
#Her yüz için duygu analizi yapacak (mutlu, üzgün, sinirli..)

from deepface import DeepFace
import cv2

class FaceAnalyzer:
    
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier("D:\\AcunMedya\\AcunMedya\\Python_Ile_Veri_Bilimi_Nisan_3_ve_Nisan_4_Hafta_Odevi\\Nisan_4_Hafta\\haarcascade_frontalface_default.xml")

    def detect_faces(self,frame):
        #OpenCV Haarcascade kullanarak frame içindeki yüzleri tespit eder.
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        return faces


    def analyze_faces(self,frame):
        try:
            results = DeepFace.analyze( #Kameradaki kareyi tarar ve yüzleri
                frame,
                actions=["emotion"], #Sadece duyguları bulsun, yaş,cinsiyet,ırka gerek yok
                enforce_detection=False #yüz yoksa hata vermesin,boş liste dönsün
            )
            if not isinstance(results,list):
                results = [results]
            return results
        
        except Exception as e:
            print(f"Yüz analizi sırasında hata oluştu: {e}")
            return []


