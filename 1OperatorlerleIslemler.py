"""
Bölüm 1: Operatörler ile İşlemler
✅ Görev 1: Kullanıcıdan iki sayı alıp, aşağıdaki işlemleri yaparak ekrana yazdıran bir Python programı yazın:

Toplama (+)
Çıkarma (-)
Çarpma (* )
Bölme (/)
Mod alma (%)
Üs alma (** )
📌 İpucu: input() ile kullanıcıdan veri alabilir, int() veya float() ile dönüştürebilirsiniz.
"""
sayi1 = int(input("Birinci sayiyi giriniz: "))
sayi2 = int(input("Ikinci sayiyi giriniz: "))

toplam = sayi1 + sayi2
fark = sayi1 - sayi2
carpim = sayi1*sayi2
us_islemi = sayi1**sayi2

print("Sayilarin toplami: ",toplam)
print("Sayilarin farki: ",fark)
print("Sayilarin carpimi: ",carpim)
if sayi2!=0:
    bolum=sayi1/sayi2
    print("Sayilarin bolumu: ",bolum)
else:
    print("Ikinci sayi 0 oldugu icin bolum yapılamaz!")
if sayi2==0:
    print("Ikinci sayi 0 oldugu icin mod islemi yapilamaz.")
else:
    mod = sayi1%sayi2
    print("Sayi1'in sayi2'ye gore modu: ",mod)

print("Sayi1 ussu sayi2: ",us_islemi)