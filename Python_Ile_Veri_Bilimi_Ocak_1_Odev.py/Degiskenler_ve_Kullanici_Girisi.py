"""
Soru: Kullanıcıdan adını, soyadını ve yaşını alan bir Python programı yazın. 
Alınan bilgileri şu formatta ekrana yazdırın:
"Merhaba [Ad Soyad], [Yaş] yaşındasınız. Hoş geldiniz!"
"""

def kullanici():
    ad = input("Adınızı giriniz:")
    soyad = input("Soyadınızı giriniz:")
    yas = input("Yaşınızı giriniz:")

    print(f"Merhaba {ad} {soyad}, {yas} yaşındasınız. Hoşgeldiniz!")

kullanici()