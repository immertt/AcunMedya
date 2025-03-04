"""
Döngüler (for ve while)
Soru: Kullanıcıdan bir sayı alarak 1’den bu sayıya kadar olan tüm sayıların toplamını
hesaplayan bir Python programı yazın. Programda hem for hem de while döngüsü kullanarak 
iki farklı yöntemle sonucu ekrana yazdırın.
"""

#for döngüsü
"""
toplam = 0
sayi = int(input("Bir sayi giriniz:"))
for i in range(sayi+1): #range 0dan o sayiya kadar olan sayıları alır.
    toplam+=i
print(f"Sayiların toplamı:{toplam}")
"""

#while döngüsü
"""
sayi = int(input("Bir sayi giriniz:"))
toplam = 0
i=1
while(i<=sayi):
    toplam+=i
    i=i+1
print(f"Sayiların toplamı:{toplam}")
"""