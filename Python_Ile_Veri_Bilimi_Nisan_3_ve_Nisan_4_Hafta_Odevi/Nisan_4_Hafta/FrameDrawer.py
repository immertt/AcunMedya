import cv2

class FrameDrawer:
    def __init__(self):
        pass

    def draw_labelled_box(self, frame, x, y, w, h, label="Gülümsüyor"):
        #Koordinatlara kutu çiz ve yazı yaz
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #x,y,w,h degerleri yüzün koordinatlarını alır,rectangle dikdörtgen çizer,putText yazı yazar.
        text_position = (x, y + h + 25)

        cv2.putText(
            frame,
            label,
            text_position,
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )
        return frame