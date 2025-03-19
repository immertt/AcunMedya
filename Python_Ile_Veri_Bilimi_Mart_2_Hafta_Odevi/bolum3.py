"""
📉 BÖLÜM 3: Ürün Satış Analizi
📌 Görev 4:

Bir mağazada 1 ay boyunca satılan 5 farklı ürünün günlük satış miktarlarını simüle edin.
Ürünlerin adları: "Telefon", "Bilgisayar", "Kulaklık", "Saat", "Tablet"
Her ürün için 30 günlük rastgele satış değerleri üretin (10-100 arası değişebilir).
Her ürünün toplam ve ortalama satış miktarlarını hesaplayın.
Ürün bazında bir çubuk grafiği çizin.

"""
import numpy as np
import matplotlib.pyplot as plt

urunler = np.array(["Telefon","Bilgisayar","Kulaklık","Saat","Tablet"])

satis_miktarlari = np.random.randint(10,101,size = (5,30)) #5 ürün 30 gün 

toplam_satis = satis_miktarlari.sum(axis=1)
ort_satis = satis_miktarlari.mean(axis=1)

for i in range(len(urunler)):
    print(f"\n{urunler[i]}\nToplam Satış Miktarı:{satis_miktarlari[i].sum()}\nOrtalama Satış Miktarı:{ort_satis[i]:.2f}")

plt.figure(figsize=(10, 5))
plt.bar(urunler, toplam_satis, color=['blue', 'green', 'red', 'purple', 'orange'], alpha=0.7)
plt.xlabel("Ürünler")
plt.ylabel("Toplam Satış Miktarı")
plt.title("Ürün Bazında Toplam Satışlar")
plt.show()    