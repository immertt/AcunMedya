kullanicilar = []

ad=input("Adınızı girin: ")
soyad=input("Soyadınız girin: ")
kullanici = {
    "Ad":ad,
    "Soyad":soyad
}
kullanicilar.append(kullanici)


with open("kullanicilar.json","w",encoding="utf-8") as dosya:
    x = json.load(dosya)









