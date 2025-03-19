"""
Ödev Konusu: Bu ödev kapsamında, Python'da Nesne Yönelimli Programlama (OOP) prensiplerini 
kullanarak derste oluşturulan main.py dosyasını tamamlamanız gerekmektedir. 
Ödevi tamamlarken aşağıdaki gerekliliklere dikkat etmelisiniz.

✅GitHub Kullanımı:
Ödevinizi GitHub üzerinden bir repository (repo) oluşturarak paylaşmanız gerekmektedir.
Repo içerisinde projenizin tüm dosyaları yer almalıdır.
Ödev dosyanızın içinde repo linkinizi belirtmeniz zorunludur.
Klonlanması gereken repo linki -> https://github.com/ahmetKaya00/Python-Veri-Bilimi-AcunMedya---1

✅Proje Yapısı:
Size verilen projede main.py dosyasında eksik kodları tamamlayarak çalışır hale getirmeniz gerekmektedir.
Projede, OOP prensipleri olan sınıflar (classes), nesneler (objects), kapsülleme (encapsulation), 
kalıtım (inheritance) ve çok biçimlilik (polymorphism) gibi temel bileşenleri kullanmalısınız.

✅Ödev Dosya Formatı:
Tamamladığınız main.py kodundaki her fonksiyonun ayrı ekran görüntüsünü  alarak ödev raporunuza ekleyiniz.
5 adet teorik soru ve cevaplarını raporunuza yazınız.

‼‼Ödev raporunu PDF formatında teslim ediniz ve sisteme yükleyiniz. 


"""

#☑𝐏𝐘𝐓𝐇𝐎𝐍'𝐃𝐀 𝐁𝐈𝐑 𝐒𝐈𝐍𝐈𝐅 (𝐂𝐋𝐀𝐒𝐒) 𝐍𝐀𝐒𝐈𝐋 𝐓𝐀𝐍𝐈𝐌𝐋𝐀𝐍𝐈𝐑 𝐕𝐄 𝐁𝐈𝐑 𝐍𝐄𝐒𝐍𝐄 (𝐎𝐁𝐉𝐄𝐂𝐓) 𝐍𝐀𝐒𝐈𝐋 𝐎𝐋𝐔Ş𝐓𝐔𝐑𝐔𝐋𝐔𝐑? 
#𝐊𝐎𝐃 Ö𝐑𝐍𝐄Ğ𝐈 𝐈𝐋𝐄 𝐀Ç𝐈𝐊𝐋𝐀𝐘𝐈𝐍

#Python'da sınıf kavramı(class) nesnelerin özelliklerinin barındırıldıgı bir alandır. Nesne denilen şey
#ise bu sınıftan türetilen bir örnektir.

class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def bilgileri_al(self):
        print(f"{self.marka} {self.model} {self.yil}")


araba = Araba("Ford","Focus",2021) #nesne oluşturduk.
araba.bilgileri_al() #sınıf içerisindeki fonksiyonu cagırdık.


#☑𝐄𝐍𝐂𝐀𝐏𝐒𝐔𝐋𝐀𝐓𝐈𝐎𝐍 (𝐊𝐀𝐏𝐒Ü𝐋𝐋𝐄𝐌𝐄) 𝐍𝐄𝐃𝐈𝐑? 𝐏𝐘𝐓𝐇𝐎𝐍'𝐃𝐀 𝐍𝐀𝐒𝐈𝐋 𝐔𝐘𝐆𝐔𝐋𝐀𝐍𝐈𝐑? 𝐊𝐎𝐃 Ö𝐑𝐍𝐄Ğ𝐈 𝐈𝐋𝐄 𝐀Ç𝐈𝐊𝐋𝐀𝐘𝐈𝐍.

#Encapsulation kavramı, sınıf içerisindeki degisken veya metotların dışarıdan dogrudan erişilmesinin
#kapatılmasıdır.Encapsulation bir güvenlik görevlisi gibi düşünülebiri.

class Hesap:
    def __init__(self, hesap_no, bakiye):
        self.hesap_no = hesap_no
        self.__bakiye = bakiye  #encapsulation yapılıyor.

    def bakiye_goster(self):
        print(f"Hesap No: {self.hesap_no}, Bakiye: {self.__bakiye} TL")
    #bu fonksiyonu self.__bakiye yapamadıgımız icin kullanıyoruz.    

    def para_cek(self, miktar):
        if miktar > self.__bakiye:
            print("Para yok")
        else:
            self.__bakiye -= miktar
            print(f"{miktar} TL çekildi.")

hesap = Hesap("123456", 5000)
hesap.bakiye_goster()
hesap.para_cek(1000)
hesap.para_cek(5000) #Para yok

print(hesap.__bakiye)  # hata alırız.

#☑𝐏𝐘𝐓𝐇𝐎𝐍'𝐃𝐀 𝐈𝐍𝐈𝐓 𝐌𝐄𝐓𝐎𝐃𝐔𝐍𝐔𝐍 𝐆Ö𝐑𝐄𝐕𝐈 𝐍𝐄𝐃𝐈𝐑?

#__init__ metodu diger adıyla constructor metot olarak geçer. Sınıf veya sınıftan bir nesne cagrıldıgında
#mutlaka çalışacak olan metottur.

def __init__(self, hesap_no, bakiye):
        self.hesap_no = hesap_no
        self.__bakiye = bakiye  #encapsulation yapılıyor.
#Hesap sınıfını cagırdıgımda "hesap_no" ve "bakiye" alanlarını mutlaka görmeliyim.


#☑𝐈𝐍𝐇𝐄𝐑𝐈𝐓𝐀𝐍𝐂𝐄 (𝐊𝐀𝐋𝐈𝐓𝐈𝐌) 𝐍𝐄𝐃𝐈𝐑? 𝐏𝐘𝐓𝐇𝐎𝐍'𝐃𝐀 𝐍𝐀𝐒𝐈𝐋 𝐊𝐔𝐋𝐋𝐀𝐍𝐈𝐋𝐈𝐑? 𝐊𝐎𝐃 Ö𝐑𝐍𝐄Ğ𝐈 𝐈𝐋𝐄 𝐀Ç𝐈𝐊𝐋𝐀𝐘𝐈𝐍

#Inheritance kelime anlamı olarak miras almak demektir. Cocuk sınıfın ata sınıfın özelliklerini
#alması olarak da adlandırabiliriz.

class Hayvan():
    def __init__(self, isim):
        self.isim = isim

    def ses_cikar(self):
        print("Hayvan ses çıkarıyor.")

    def yuru(self):
        print("Yürüme işi yapılıyor.")    

class Kedi(Hayvan): #Kedi sınıfı(cocuk) Hayvan sınıfından(ata) miras alıyor 
    def ses_cikar(self):
        print("Miyavv")

class Kopek(Hayvan): #Koek sınıfı(cocuk) Hayvan sınıfından(ata) miras alıyor
    def ses_cikar(self):
        print("Hav havv")

kedi = Kedi("Pamuk")
kopek = Kopek("Karabaş")

kedi.yuru()
kopek.yuru()
kedi.ses_cikar()
kopek.ses_cikar()

#☑𝐏𝐎𝐋𝐘𝐌𝐎𝐑𝐏𝐇𝐈𝐒𝐌 (Ç𝐎𝐊 𝐁𝐈Ç𝐈𝐌𝐋𝐈𝐋𝐈𝐊) 𝐍𝐄𝐃𝐈𝐑? 𝐏𝐘𝐓𝐇𝐎𝐍'𝐃𝐀 𝐍𝐀𝐒𝐈𝐋 𝐔𝐘𝐆𝐔𝐋𝐀𝐍𝐈𝐑? 𝐊𝐎𝐃 Ö𝐑𝐍𝐄Ğ𝐈 𝐈𝐋𝐄 𝐀Ç𝐈𝐊𝐋𝐀𝐘𝐈𝐍

#Çok çeşitlilik anlamına gelir. Aynı isimli fonksiyonun farklı sınıflarda farklı şekilde çalışmasıdır.

class Kus:
    def uc(self):
        print("Kuş uçuyor.")

class Ucak:
    def uc(self):
        print("Uçak havalanıyor.")

def havalan(obj): #içerisine obje alıyor obje tüm nesnelerin atasıdır. Her şey aslında objedir.
    obj.uc()

kus = Kus()
ucak = Ucak()

#Burada aynı metot farklı iki işlevi yerine getiriyor.
havalan(kus)
havalan(ucak)