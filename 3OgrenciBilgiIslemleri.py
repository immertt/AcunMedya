ogrenciler = []

#ogrenci ekleme işlemi yapıldı, ogrenci bilgisi sözlükte saklandı ve listeye eklendi.
def ogrenci_ekle():
    ad = input("Adınızı giriniz:\n")
    soyad = input("Soyadınızı giriniz:\n")
    numara = input("Numaranızı giriniz:\n")
    bolum = input("Bölümünüzü giriniz:\n")
    not_ortalama = input("Not ortalamanızı giriniz:\n")

    ogrenci = {
        "Ad": ad,
        "Soyad" : soyad,
        "Numara" : numara,
        "Bolum" : bolum,
        "Not ortalama" : not_ortalama
    }
    ogrenciler.append(ogrenci)
    print(f"{numara} numaralı ögrenci sisteme başarıyla eklendi.")

#eklenen ögrencileri listelemek için kullanılır.
def ogrenci_listele():
    if not ogrenciler:
        print("Ogrenci bulunamadı.")
        return
    for ogrenci in ogrenciler:
        print(ogrenci)

#ogrenci guncellemek ve bulmak icin oncelikle o ogrenciye erişmemiz gerekir.Bunun için de onu bulmalıyız.
def ogrenci_bul(numara):
    for ogrenci in ogrenciler:
        if ogrenci["Numara"] == numara:
            return ogrenci
    return None

#ogrencinin herhangi bir bilgisini günceller.
def ogrenci_guncelle():
    ogr_num = input("Güncellemek istediginiz ogrencinin numarasını giriniz:\n")
    ogrenci = ogrenci_bul(ogr_num)
    if ogrenci:
        bilgi = int(input("Ögrencinin hangi bilgisini güncellemek istiyorsunuz:\n1.Ad\n2.Soyad\n3.Bolum\n4.Ortalama\n "))
        if bilgi==1:
            ogrenci["Ad"] = input("Ogrencinin adını giriniz:\n")
        elif bilgi==2:
            ogrenci["Soyad"] = input("Ogrencinin soyadını giriniz:\n")
        elif bilgi==3:
            ogrenci["Bolum"] = input("Ogrencinin bolumunu giriniz:\n")
        elif bilgi==4:
            ogrenci["Not ortalama"] = input("Ogrencinin not ortalamasını giriniz:\n")
        else:
            print("Geçersiz bir işlem!")        
    else:
        print("Ögrenci bulunamadı.")

#ogrenci silme işlemi için kullanılır.
def ogrenci_sil():
    ogr_num = input("Silmek istediginiz ogrencinin numarasını giriniz:\n")
    ogrenci = ogrenci_bul(ogr_num)
    if ogrenci:
        ogrenciler.remove(ogrenci)
        print("Ögrenci silindi.")
    else:
        print("Ögrenci bulunamadı.")

#uygulama için basit bir arayüz oluşturmak için menü fonksiyonu kullanıldı.
def menu():
    while True:
        print("1. Ogrenci Ekle\n2.Ogrenci Güncelle\n3.Ogrenci Sil\n4.Ogrenci Listele\n5.Çıkış")
        secim = int(input("Bir seçim yapınız\n"))
        if secim==1:
            ogrenci_ekle()
        elif secim==2:
            ogrenci_guncelle()
        elif secim==3:
            ogrenci_sil()
        elif secim==4:
            ogrenci_listele()
        elif secim==5:
            print("Çıkış yapılıyor..")
            break
        else:
            print("Geçersiz bir işlem.") 
menu()







