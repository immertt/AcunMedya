"""
2. Günlük Kayıt Defteri
📌 Görev:

Kullanıcıdan aldığı notları "gunluk.txt" dosyasına ekleyen bir program yazın.
Kullanıcı "goruntule" komutunu girerse, dosyada kayıtlı tüm notları ekrana yazdırın.
Kullanıcı "sil" yazarsa "gunluk.txt" dosyasını silin.
💡 İpucu: os.remove("gunluk.txt") komutunu kullanabilirsiniz.
"""
import os

def gunluk_yaz():
    with open("gunluk.txt","a",encoding="utf-8") as dosya:
        veri=input("Istediginiz notu yazabilirsiniz:\n")
        dosya.write(veri +"\n")

def gunluk_goruntule():
        #dosya yokken okumaya çalışırsak hata alırız, o yüzden try except kullanmalıyız
    try:    
        with open("gunluk.txt","r",encoding="utf-8") as dosya:
            icerik = dosya.read()
            if icerik:
                print("Dosyanın Icerigi\n")
                print(icerik)
            else:
                print("Dosya boş")
    except FileNotFoundError:
        print("Dosya bulunamadı.")            

def gunluk_sil():
    #dosya yokken silemeyiz,o yüzden try except kullanmalıyız
    try:
        if "gunluk.txt":
            os.remove("gunluk.txt")
        else:
            print("Dosya bulunamadı...")
    except FileNotFoundError:
        print("Olmayan dosyayı silemezsin")        

while True:
    secim = input("1-)Gunluk yaz\n2-)Gunluk goruntule\n3-)Gunluk sil\n4-)Cikis\n")
    if secim == "1":
        gunluk_yaz()
    elif secim == "2":
        gunluk_goruntule()
    elif secim == "3":
        gunluk_sil()
    elif secim == "4":
        exit()            
    else:
        print("Hata")





