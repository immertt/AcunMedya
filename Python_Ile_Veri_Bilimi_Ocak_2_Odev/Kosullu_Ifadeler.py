"""
Soru: Kullanıcıdan bir sayı alarak, bu sayının çift mi tek mi olduğunu ekrana yazdıran 
bir Python programı yazın. Eğer sayı negatifse, ekrana "Negatif sayı girdiniz!" mesajı versin.
"""
sayi = int(input("Bir sayi giriniz:"))

if sayi < 0:
    print("Negatif sayı girdiniz!")
    if sayi % 2 == 0:
        print("Girdiğiniz sayı çifttir.")
elif sayi == 0:
    print("Sayi 0 ve çifttir")    
else:
    print("Pozitif sayı girdiniz!")
    if sayi % 2 == 0:
        print("Girdiğiniz sayı çifttir.")