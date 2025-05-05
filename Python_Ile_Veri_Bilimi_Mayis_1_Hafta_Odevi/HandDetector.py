import cv2
import mediapipe as mp

#El tespiti yapıp landmarkları döndürecegiz,el üzerine landmark çizimleri,landmark koordinatları.
class HandDetector:
    def __init__(self,mode=False,max_hands=2,detection_confidence=0.5,tracking_confidence=0.5):
        #aynı elde sürekli el var mı,diye kontrol etmez.
        self.mode = mode
        self.max_hands = max_hands # max kaç el olsun ?
        self.detection_confidence = detection_confidence #güven oranı
        self.tracking_confidence = tracking_confidence #bulunan eli takip edilmesi

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode = self.mode,
            max_num_hands = self.max_hands,
            min_detection_confidence = self.detection_confidence,
            min_tracking_confidence = self.tracking_confidence
        )
        self.mp_draw = mp.solutions.drawing_utils


    def detect_hands(self,frame):
        img_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = self.hands.process(img_rgb)
        return results


    def draw_landmarks(self,frame,hand_landmarks):
        self.mp_draw.draw_landmarks(frame,hand_landmarks,self.mp_hands.HAND_CONNECTIONS)


    def get_landmarks_list(self,frame,hand_landmarks): #elin 21 landmark'ını döner(0,1,2,3,..21)
        #id=0 lm-> bilek noktası,id=1 lm->başparmak 1.bogum.....
        #lm x,y,z degerlerini tutar. lm.x->x oranı(0 ile 1 arasında),lm.y->y oranı (0 ile 1 arası)
        #lm.z-> derinlik oranı(kameradan tahmini uzaklık)
        h, w, c = frame.shape #h,w,c alma sebebimiz pixel x,y koordinatlarını bulmak!
        lm_list = []
        for id,lm in enumerate(hand_landmarks.landmark):
            cx,cy = int(lm.x*w),int(lm.y*h)
            lm_list.append((id,cx,cy)) #id=0 bilek için x,y koord., id=1 başparmak 1.bogum x,y koord.

        return lm_list #-> (0,x0,y0),....(4,x4,y4) başparmakucu, (8,x8,y8) işaretparmakucu