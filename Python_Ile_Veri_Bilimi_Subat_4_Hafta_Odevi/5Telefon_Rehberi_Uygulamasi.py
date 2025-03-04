"""
4. Telefon Rehberi Uygulaması
📌 Görev:

"rehber.txt" adlı bir dosyada telefon numaralarını saklayan bir program yazın.
Kullanıcı "ekle" komutu girerse, ad ve telefon numarası alıp dosyaya ekleyin.
Kullanıcı "ara" komutunu girerse, adı girilen kişinin telefon numarasını gösterin.
Kullanıcı "listele" komutunu girerse, tüm rehberi ekrana yazdırın.
💡 İpucu: Dosyayı satır satır okuyarak ad-soyad eşleştirmesi yapabilirsiniz.
"""
import os

def kisi_ekle():
    ad = input("Kisinin adını giriniz:")
    telno = input("Kisinin telefon numaramasını giriniz:")
    
    with open("rehber.txt","a",encoding="utf-8") as dosya:
        dosya.write(f"{ad} - {telno}\n")
    print(f"{ad} rehbere eklendi..")

def kisi_bul():
    aranan = input("Aramak istediginiz kişinin adını giriniz:\n")
    if not aranan.strip():
        print("Hatalı giriş! Lütfen geçerli bir isim girin.")
        return  
    try:
        with open("rehber.txt","r",encoding="utf-8") as dosya:
            kisiler = dosya.readlines()
            #strip() fonksiyonu baştaki ve sondaki boşlukları siler
            #lower() fonksiyonu büyük küçük harf duyarlılıgını kaldırır hepsini küçük harf yapar.
            bulunanlar = [kisi.strip() for kisi in kisiler if kisi.lower().startswith(aranan.lower())]
            if bulunanlar:
                print("Bulunan Kayıtlar:")
                for kisi in bulunanlar:
                    print(kisi)  # break olmadan tüm eşleşmeleri göster
            else:
                print("Aranan kişi rehberde bulunamadı.")
            
    except FileNotFoundError:
        print("Rehberde kimse yok..")    

def kisileri_listele():
    try:
        with open("rehber.txt","r",encoding="utf-8") as dosya:
            icerik = dosya.readlines()
            
            if not icerik:
                print("Rehberde kimse yok..")
                return    
            print("Rehber Listesi\n")
            for satir in icerik:
                print(satir.strip())
    except FileNotFoundError:
        print("Rehber bulunamadı..")            

#Ek olarak rehberi silelim.
def rehber_sil():
    try:
        if "rehber.txt":
            os.remove("rehber.txt")
            print("Rehber başarıyla silindi")
        else:
            print("Dosya bulunamadı.")
    except FileNotFoundError:
        print("Dosya bulunamadı")   
def menu():
    while True:
        print("Bir seçim yapınız\n")
        secim = input("1-)Kişi Ekle\n2-)Kişi Bul\n3-)Kişileri Listele\n4-)Rehberi Sil\n5-)Çıkış\n")
        if secim == "1":
            kisi_ekle()
        elif secim == "2":
            kisi_bul()
        elif secim == "3":
            kisileri_listele()
        elif secim == "4":
            rehber_sil()    
        elif secim == "5":
            exit()
        else:
            print("Hatalı tuşlama yaptınız..")

menu()            