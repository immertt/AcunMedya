#Pandas Kütüphanesi
import pandas as pd

#Veri setini indirdim, dataframe attım.
df = pd.read_csv("D:\\AcunMedya\\AcunMedya\\Python_Ile_Veri_Bilimi_Mart_3_Hafta_Odevi\\heart.csv")

#Verinin ilk 5 satırını görüntüleyelim.
print(df.head())

#Veri Seti Bilgisini görebiliriz.
print(df.info())

#Eksik verilerin sayısını görebiliriz. Bizim veri setimizde eksik bir veri yok.
print(df.isnull().sum())

#Temel İstatistikleri görelim. #count,mean,std,çeyreklikler ve max verileri.
print(df.describe())