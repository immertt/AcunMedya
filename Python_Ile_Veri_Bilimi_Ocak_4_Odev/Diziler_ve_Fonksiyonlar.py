"""
Diziler ve Fonksiyonlar
Soru: Kullanıcıdan 5 adet tam sayı alarak bir listeye ekleyen ve ardından bu sayıların 
en büyüğünü ve en küçüğünü bulan bir Python programı yazın. Bu işlemi gerçekleştiren bir 
fonksiyon tanımlayın ve çağırarak sonucu ekrana yazdırın.
"""
def min_max_bul():
    sayilar = []
    for i in range(5):
        sayi = int(input(f"{i+1}. sayıyı girin: "))
        sayilar.append(sayi)
    
    en_kucuk = min(sayilar)
    en_buyuk = max(sayilar)
    
    print(f"Girilen sayılar: {sayilar}")
    print(f"En küçük sayı: {en_kucuk}")
    print(f"En büyük sayı: {en_buyuk}")

min_max_bul()

