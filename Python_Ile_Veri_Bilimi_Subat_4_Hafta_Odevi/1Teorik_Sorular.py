"""
ÖDEV: Dosya İşlemleri Üzerine Uygulamalı Çalışma
Ödevin Amacı:
Bu ödev, Python'da dosya açma, okuma, yazma, silme ve JSON işlemleri 
gibi temel dosya işlemlerini pekiştirmenize yardımcı olacaktır. 
Aynı zamanda dosya işlemleriyle uygulamalı küçük projeler geliştirmenizi sağlayacaktır.
"""

#BÖLÜM 1: Teorik Sorular

#Q1-)Dosya açma modları (r, w, a, x, b, t) nedir ve hangi durumlarda kullanılır?
#Q2-)Bir dosyayı okurken read(), readline() ve readlines() arasındaki farklar nelerdir?
#Q3-)Dosya işlemlerinde with open(...) kullanmanın avantajları nelerdir?
#Q4-)JSON formatı nedir ve hangi durumlarda kullanılır?
#Q5-)Bir dosyanın var olup olmadığını kontrol etmek için hangi Python modülü kullanılır? Örnek kod ile açıklayınız.


#A1-)
#r mode : Dosya okumak için kullanılır -> read
#w mode : Dosyaya yazmak için kullanılır, dosya yoksa oluşturur varsa içerigini siler ve yazar.
#a mode : Daha güvenlidir. w mode ile aynıdır fakat dosyanın içerigini silmez, sonuna ekleme yapar.
#x mode : Dosya yoksa oluşturur, varsa hata verir.
#b mode : Binary mode'dur. Dosyanın binary olarak açılmasını saglar.
#t mode : Text mode'dur. Dosyanın metin olarak işlenmesini saglar.

#A2-)
#read(size) -> Dosyanın boyutun belirtilmedigi sürece tamamını okur.
#readline() -> Satır satır okuma gerçekleştirilir.Döngüseldir.
#readlines() -> Dosyanın tüm satırlarını liste olarak döndürür.

#A3-)
#with open() kullanıldıgında dosyayı kapatmak için close() metoduna gerek yoktur, otomatik kapatılır.
#Herhangi bir hata olması durumunda dosyayı kapatır.
#Az ve temiz kod kullanımı saglar.

#A4-)
#JSON bir veri formatıdır. Key-Value ilişkisi ile okunaklı bir yapıya sahiptir.
#Web uygulamaları arasında veri alışverişinde kullanılır
#Veri setlerini taşımak ve analiz etmek için kullanılır.
#Örnek Kullanım
"""
import json
with open("veri.json","r",encoding="utf-8") as dosya:
    veri = json.load(dosya) #json dosyasını oku ve sözlüge çevir.
    print(veri["ad"])
"""

#A5-)
#Dosyanın var olup olmadıgını "os" kütüphanesiyle anlayabiliriz.
#os.path.exists(dosyayolu) ile dosya veya dizin kontrol edilir.
#os.path.isfile() komutu ile de dosyanın var olup olmadıgını ogrenebiliriz.
#Örnek Kullanım
"""
import os
dosya yolu = "dosya.txt"
if os.path.isfile(dosyayolu):
    print("Bu bir dosyadır.")
else:
    print("Dosya veya dizin bulunamadı.")    
"""




