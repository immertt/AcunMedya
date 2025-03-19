"""
📌 Görev 1:

Bir şirkette çalışan 500 kişinin maaşlarını simüle edin.
Maaşlar 3000 TL ile 15000 TL arasında rastgele belirlenecek.
Ortalama, maksimum ve minimum maaşları hesaplayın.
Maaş dağılımını histogram ile görselleştirin.

📌 Görev 2:

500 çalışanı 3 farklı departmana rastgele atayın:
1 = Mühendislik
2 = Muhasebe
3 = Pazarlama
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
maaslar = np.random.randint(3000,15001,500)

print("Minimum Maaş: ",np.min(maaslar))
print("Maximum Maaş: ",np.max(maaslar))
print("Ortalama Maaş:",np.mean(maaslar))

departmanlar = np.random.choice([1,2,3],size=500)
muhendislik = np.sum(departmanlar==1)
muhasebe = np.sum(departmanlar==2)
pazarlama = np.sum(departmanlar==3)

print(f"\nMühendislik:{muhendislik} kişi")
print(f"Muhasebe:{muhasebe} kişi")
print(f"Pazarlama:{pazarlama} kişi")

plt.figure(figsize=(10,5))
plt.hist(maaslar,bins=15,edgecolor="black",alpha=0.7)
plt.xlabel("Maaş aralıkları")
plt.ylabel("Çalışan Sayısı")
plt.title("Maaş Not Dagilimi")
plt.grid(True)
plt.show()