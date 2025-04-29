class SmileDetector:

    def __init__(self):
        pass

    def is_smiling(self,analysis_result):
        #Deepface analizi yapılınca gelen deger girilir, domaninat emotion happy ise true döner
        if analysis_result is None:
            return False
        
        dominant_emotion = analysis_result.get("dominant_emotion","")
        return dominant_emotion.lower() == "happy"
    