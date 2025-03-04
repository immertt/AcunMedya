def gunluk_yaz():
    with open("veri.txt","w",encoding="utf-8") as dosya:
        x = input("Gunlugu yazınız:\n")
        dosya.write(x)

def gunluk_goster():
    with open("veri.txt","r",encoding="utf-8") as dosya:
        icerik = dosya.read
        if icerik:
            print(icerik)
        else:
            print("Dosya yok")    

gunluk_yaz()
gunluk_goster()











