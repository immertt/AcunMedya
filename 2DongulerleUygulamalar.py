#✅ Görev 2: Kullanıcıdan bir sayı alarak 1’den o sayıya kadar olan sayıların 
#toplamını hesaplayan bir Python programı yazın. (For veya While döngüsü kullanın.)

sayi = int(input("Pozitif bir sayi giriniz: "))
toplam=0
#range sayi'ya kadar olan sayilari alir, sayinin kendisini dahil etmez. Sayi 5 olursa 5'i toplamaya dahil etmez.
for i in range(sayi + 1):
    toplam+=i
print("Sayilarin toplami: ",toplam)

#✅ Görev 3: 1 ile 100 arasındaki çift sayıları ekrana yazdıran bir Python programı yazın.

#range içerisinde virgülden önceki sayi hangi sayi ile baslayacagımızı soyler.
for i in range(1,100):
    if i%2==0:
        print(i)


#✅ Görev 4: Kullanıcıdan alınan bir metni ters çeviren ve
# ekrana yazdıran bir Python programı yazın. (Döngü kullanarak yapın.)

"""
Bu işlem stringlerde yapılır. text[start:stop:step] işlemi olarak geçer.
start -> baslangic indexi
stop -> bitis indexi
step -> atlama
text = acunmedya olsaydı ve text[1:5:1] işlemi yapılsaydı bunun sonucu şu olurdu:
"cunm" -> 1.indexi alır, 5. indexe kadar gelir, 5. indexi almaz ver teker teker atlar.
text[1:5:2] olsaydı sonuc su olurdu:
cn -> 1'den başladı. ikiser ikiser atlayacagımız icin 'u' harfini almadı....
"""
text = input("Bir kelime yazınız: ")
print("Girilen kelimenin tersi: ",text[::-1])




