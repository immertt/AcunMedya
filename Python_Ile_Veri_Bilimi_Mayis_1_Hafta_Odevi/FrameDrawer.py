import cv2


class FrameDrawer:
    def __init__(self):
        pass

    def draw_text(self, frame, text, position=(10, 70), font_scale=1, color=(0, 255, 0), thickness=2):
        """
        Frame üzerine yazı ekler.
        frame: Görüntü/frame
        text: Yazılacak metin
        position: (x, y) pozisyonu
        font_scale: Yazı boyutu
        color: Yazı rengi(B,G,R)
        thickness: Çizgi kalınlığı
        """
        cv2.putText(frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness)

    def draw_labelled_box(self, frame, x, y, w, h, label=""):
        """
        Frame üzerine etiketli kutu çizer.
        frame: Görüntü/frame
        x, y, w, h: Dikdörtgenin sol üst koordinatı ve genişlik/yükseklik
        label: Kutu üstüne yazılacak etiket
        """
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.rectangle(frame, (x, y - 30), (x + w, y), (0, 255, 0), -1)
        cv2.putText(frame, label, (x + 5, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)