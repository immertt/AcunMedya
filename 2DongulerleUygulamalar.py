

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




