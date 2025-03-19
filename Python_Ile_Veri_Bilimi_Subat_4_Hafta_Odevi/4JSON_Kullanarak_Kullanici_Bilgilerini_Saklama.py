"""
3. JSON Kullanarak Kullanıcı Bilgileri Saklama
📌 Görev:

"kullanicilar.json" adlı bir dosya oluşturun.
Kullanıcıdan ad, soyad ve yaş bilgilerini alıp JSON formatında kaydedin.
Kullanıcının "listele" komutunu girdiğinde JSON dosyasındaki tüm kullanıcıları ekrana yazdırın.
💡 İpucu: json.dump() ve json.load() fonksiyonlarını kullanabilirsiniz.
"""
#Kullanıcı bilgilerini JSON dosyasına kaydetmek için json.dump()
#JSON dosyasındaki verileri okumak için json.load()

import json

def kullanici_ekle():
    ad = input("Adınızı giriniz:")
    soyad = input("Soyadınızı giriniz:")
    yas = input("Yasinizi giriniz")
    
    kullanici = {
        "Ad": ad,
        "Soyad":soyad,
        "Yas":yas
    }
    try:
        with open("kullanicilar.json","r+",encoding="utf-8") as dosya:
            try:
                veri = json.load(dosya) #Dosyadaki veriyi oku
            except json.JSONDecodeError: #eger veri yoksa veya yanlıs formattaysa               
                veri = []  

            veri.append(kullanici) #kullanici bilgilerini veriye ekle.
            dosya.seek(0) #dosyanın başına git
            json.dump(veri,dosya,indent=4,ensure_ascii=False) #dosyayı yaz ve kaydet
            print("Kullanıcı başarıyla eklendi.")

    except FileNotFoundError:
        #Dosya yoksa yeni olustur ve kullanıcıyı ekle.
        with open("kullanicilar.json","w",encoding="utf-8") as dosya:
            json.dump([kullanici],dosya,indent=4,ensure_ascii=False)
            print("Dosya oluşturuldu ve kullanıcı eklendi.")

def kullanici_listele():
    try:
        with open("kullanicilar.json","r",encoding="utf-8") as dosya:
            kullanicilar = json.load(dosya)
            print("Kullanıcılar Listesi\n")
            for kullanici in kullanicilar:
                print(f"Ad: {kullanici['Ad']}, Soyad:{kullanici['Soyad']}, Yas:{kullanici['Yas']}")

    except FileNotFoundError:
        print("Kullanıcı eklenmemiş, dosya bulunamadı.")

while True:
    secim = input("1-)Kullanici Ekle\n2-)Kullanicilari Listele\n3-)Çıkış\nSeçiminizi giriniz: ")
    if secim == "1":
        kullanici_ekle()
    elif secim == "2":
        kullanici_listele()
    elif secim == "3":
        exit()
    else:
        print("Hatalı seçim..")            