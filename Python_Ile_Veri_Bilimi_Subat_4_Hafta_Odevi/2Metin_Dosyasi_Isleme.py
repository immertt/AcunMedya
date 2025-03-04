"""
1. Metin Dosyası İşleme
📌 Görev:

"ogrenciler.txt" adlı bir dosya oluşturun.
Kullanıcıdan öğrenci isimleri alarak bu dosyaya ekleyin.
Kullanıcı "bitti" yazdığında giriş işlemini sonlandırın.
Dosyadaki öğrenci isimlerini ekrana yazdıran bir fonksiyon yazın.
💡 İpucu: open("ogrenciler.txt", "a") kullanabilirsiniz.
"""
def ogrenci_ekle():
    with open("ogrenciler.txt","a",encoding="utf-8") as dosya:
        veri = input("Ogrenci ismini giriniz:\n")
        if not veri:
            print("Hatalı giriş! Lütfen geçerli bir isim girin.")
            return  
        dosya.write(veri +"\n")
        print("Ogrenci basarıyla eklendi.")

def ogrenci_yazdir():
    #dosya yokken okumaya çalışırsak hata alırız, o yüzden try except kullanmalıyız
    try:
        with open("ogrenciler.txt","r",encoding="utf-8") as dosya:
            icerik = dosya.read()
            if icerik:
                print("\nDosyadaki Ögrenciler:")
                print(icerik)
            else:
                print("Dosya boş")
    except FileNotFoundError:
        print("Dosya bulunamadı.")             

while(True):
    secim = input("1-)Ogrenci ekle\n2-)Ogrenci Yazdir\n3-)Çıkış\nSeçiminizi giriniz:")
    if secim == "1":
        ogrenci_ekle()
    elif secim == "2":
        ogrenci_yazdir()
    elif secim == "3":
        print("Programdan çıkılıyor...")
        exit()
    else:
        print("Hata")