#landmark listesine bakarak hangi parmaklar açık hangileri kapalı tespit etmek
#açık parmak sayısını hesaplamak, açık/kapalı parmakları bir liste olarak döndürmek
class FingerCounter:
    def __init__(self):
        self.finger_tips = [8,12,16,20]

#-> (0,x0,y0),....(4,x4,y4) baş parmak ucu, (8,x8,y8) işaret parmak ucu ....
    def count_fingers(self,lm_list,hand_label):
        fingers = []
        #Baş parmak kontrolu
        if hand_label == "Right":
            if lm_list[4][1] > lm_list[3][1]:
                fingers.append(1)
            else:
                fingers.append(0)
        else:
            if lm_list[4][1] < lm_list[3][1]:
                fingers.append(1)
            else:
                fingers.append(0)        

        for tip in self.finger_tips:
            if lm_list[tip][2] < lm_list[tip-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)    

        return fingers
    
    def get_total_fingers(self,lm_list,hand_label):
        fingers = self.count_fingers(lm_list,hand_label)
        return sum(fingers)