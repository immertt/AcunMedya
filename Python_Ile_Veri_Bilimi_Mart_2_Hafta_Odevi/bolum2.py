"""
📈 BÖLÜM 2: Hava Durumu Verileri Üretme ve Analiz
📌 Görev 3:

Bir yıl boyunca (365 gün) günlük sıcaklık değerlerini simüle edin.
Sıcaklıklar -10°C ile 40°C arasında rastgele belirlenecek.
Ortalama sıcaklığı, en sıcak ve en soğuk günü bulun.
Sıcaklık değişimlerini çizgi grafiği ile gösterin.

"""
import numpy as np
import matplotlib.pyplot as plt

sicakliklar = np.random.randint(-10,41,size=365)
en_dusuk = np.min(sicakliklar)
ort_sicaklik = np.mean(sicakliklar)
en_yuksek = np.max(sicakliklar)

print("En düşük sıcaklık degeri:",en_dusuk)
print("Ortalama sıcaklık degeri:",ort_sicaklik)
print("En yüksek sıcaklık degeri:",en_yuksek)

plt.figure(figsize=(12, 5))
plt.plot(sicakliklar,alpha=0.7)
#ortalama sıcaklıktan çizgi çekiyor.
plt.axhline(y=ort_sicaklik, color="r", linestyle="--", label="Ortalama Sıcaklık")
plt.xlabel("Gün")
plt.ylabel("Sıcaklık")
plt.title("Günlük Sıcaklık Degisimi")
plt.grid(True)
plt.show()


