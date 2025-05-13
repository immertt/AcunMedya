

class EyeTracker:
    def __init__(self):
        #IRIS landmark degerleri
        self.LEFT_IRIS = [468, 469, 470, 471]
        self.RIGHT_IRIS = [473, 474, 475, 476]


    def iris_center(self,landmarks,eye_indices,image_w,image_h):
        #Irisin merkezini bul -> landmarkları topla, 4'e böl, piksele çevir
        x = int(sum([landmarks[i].x for i in eye_indices]) / 4 * image_w)
        y = int(sum([landmarks[i].y for i in eye_indices]) / 4 * image_h)

        return x,y
    
    def analyze_eye(self,left_iris,right_iris,frame_width):
        x_avg = (left_iris[0] + right_iris[0]) / 2
        ratio = x_avg / frame_width

        if ratio < 0.46:
            direction="LEFT"
        elif ratio > 0.6:
            direction="RIGHT"
        else:
            direction="CENTER"
        
        print(f"x_avg: {x_avg:.2f}, ratio: {ratio:.3f}, direction: {direction}")

        return direction
