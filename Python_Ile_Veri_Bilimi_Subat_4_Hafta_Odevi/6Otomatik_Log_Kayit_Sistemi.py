"""
5. Otomatik Log Kayıt Sistemi
📌 Görev:

"log.txt" dosyasına her 10 saniyede bir sistemin çalıştığını kaydeden bir Python programı yazın.
Kayıtlara zaman damgası ekleyin ("%Y-%m-%d %H:%M:%S" formatında).
Kullanıcı "loglari_goruntule" yazarsa, dosyadaki tüm logları ekrana yazdırın.
💡 İpucu: time.sleep(10) fonksiyonunu kullanabilirsiniz.
"""
import os
import time
import datetime

def log_yaz():
    while True:
        #strftime metodu tarih ve saati temsil eden bir dize döndürür.
        zamani_getir = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_mesaj = f"{zamani_getir}- log mesajı\n"
        with open("log.txt","a",encoding="utf-8") as dosya:
            dosya.write(log_mesaj)

        print(f"log işlemi yapıldı: {log_mesaj}")
        time.sleep(10) #10 saniye bekleyecek ve sonra tekrar yazacak.

def log_goruntule():
    try:
        with open("log.txt","r",encoding="utf-8") as dosya:
            icerik = dosya.readlines()
            if icerik:
                print("Log Kayıtları\n")
                for satir in icerik:
                    print(satir)
            else:
                print("Dosyanın içi boş")
    except FileNotFoundError:
        print("Dosya bulunamadı.")                

def loglari_sil():
    try:
        if "log.txt":
            os.remove("log.txt")
            print("Loglar başarıyla silindi.")
        else:
            print("Log dosyası yok.")
    except FileNotFoundError:
            print("Log dosyası yok.")

def menu():
    while True:
        secim = input("1-)Log Yaz\n2-)Logları Görüntüle\n3-)logları Sil\n4-)Çıkış\n")
        if secim == "1":
            log_yaz()
        elif secim == "2":
            log_goruntule()
        elif secim == "3":
            loglari_sil()    
        elif secim == "4":
            exit()
        else:
            print("Hatalı bir tuşlama yaptınız.")            
           
menu()



