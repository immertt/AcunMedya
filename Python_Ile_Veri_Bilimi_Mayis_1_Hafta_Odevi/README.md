# El ve Parmak Tespiti Sistemi

Bu proje, Python ve OpenCV ile kameradan alınan görüntülerde el ve parmakları tespit eder ve belirli el hareketlerini komutlara çevirir.

## Özellikler:
- Çift el desteği
- Sağ/sol el ayrımı
- Açık parmak sayısına göre komut üretimi
- Dinamik metin yerleşimi
- OOP (Nesne yönelimli programlama) mimarisi

## Kullanım:
1. Projeyi klonlayın.
2. `pip install opencv-python mediapipe` komutlarıyla gerekli kütüphaneleri yükleyin.
3. `python main.py` komutuyla çalıştırın.

## Çalışma prensibi:
- Açık parmak sayısını algılar
- Belirli pozisyonlara göre `"Dur"`, `"Hazır"`, `"Yukarı"` komutlarını ekrana yazar
- Sağ ve sol eli ayırt eder

### Kontroller:
- `q` ya da `ESC` tuşu ile çıkış

---

