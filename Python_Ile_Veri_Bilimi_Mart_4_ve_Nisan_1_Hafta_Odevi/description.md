--------------------------- **Load Diabetes** Veri Seti Hakkında Bilgiler---------------------------

-Kişilerin bazı sağlık ölçümlerine bakarak, bir yıl sonraki diyabet hastalığı ilerleme skorunu tahmin etmektir.
-Bu skor, hastalığın ciddiyetini temsil eden bir sayıdır.


- 10 adet bagımsız  degiskene sahiptir->
# age(yaş), sex(cinsiyet), bmi(vücut kitle indeksi), bp(kan basıncı), s1(serum), s2, s3, s4, s5,s6
-Hedef Değişken	target: Şeker hastalığı ilerleme skoru (sürekli sayı) "amaç target'ı tahmin etmek"

# target (hedef değişken):
-Sürekli (sayısal) bir değerdir.
-Değeri yaklaşık 25 ile 350 arasında değişir.
-Bu skor bir diyabet progresyon (ilerleme) ölçüsüdür.
-Ne kadar yüksekse, kişinin diyabet durumu o kadar kötü diyebiliriz.

*
------------------------------*------------------------------*------------------------------
*
Denetimli Ögrenme ikiye ayrılır:

1.) Sınıflandırma (Classification):
    -Kan tahlil sonuçlarına göre hastalık var mı yok mu?
    -E-posta spam mi değil mi?
    -Bir müşterinin kredi alması uygun mu?
--Evet/Hayır, 0/1, Kırmızı/Mavi/Yeşil gibi

2.) Regresyon (Regression):
    -Bir evin fiyatını tahmin et.
    -Bir öğrencinin sınavdan alacağı puanı tahmin et.
    -Bir kişinin yaşını tahmin et (özelliklere göre).
--Bir evin fiyatı, bir hastanın kan şekeri düzeyi gibi


""
# Regresyon Analizinin Amacı Nedir?
- Bağımsız değişkenlerin (X) bağımlı değişken (Y) üzerindeki etkisini anlamak  
- Gelecekteki değerleri tahmin etmek
- Değişkenler arasındaki ilişkiyi modellemek
- Mesela 'oda sayısı' ve 'ev fiyatı' ifadelerinde, oda sayısı bagımsız, ev fiyatı bagımlıdır.
""

##Proje Açıklaması
Bu projede `sklearn.datasets.load_diabetes()` veri seti kullanılarak:

1) Regresyon analizi yapılması (sürekli hedef değişken için)  
2) Sınıflandırma modeli kurulması (hedef değişken sınıflara bölünüp KNN ile)  

---
##Kullanılan Yöntemler
- Lineer Regresyon → Sürekli değer tahmini  
- KNN (k-Nearest Neighbors) → Sınıf tahmini


🔹 1. Veri Seti Seçimi ve İncelemesi
-load_diabetes() veri seti kullanıldı
-Veri kümesinde 10 bağımsız değişken ve 1 adet sürekli hedef değişken (target) vardı
-Hedef: Şeker hastalığı ilerlemesi ile ilgili skor

🔹 2. Lineer Regresyon – DiabetesRegressor Sınıfı
✳️ train_simple_model(feature_name)
-Sadece tek bir özellik (örneğin bmi) kullanılarak basit lineer regresyon modeli kuruldu
-Amaç: O özelliğin target üzerindeki etkisini görmek

✳️ train_multiple_model()
-Tüm bağımsız değişkenler kullanılarak çoklu lineer regresyon modeli kuruldu
-Amaç: Bütün veriyi kullanarak daha güçlü bir model elde etmek

✳️ print_metrics()
-Her iki model için aşağıdaki metriklerle değerlendirme yapıldı:
    R² Skoru
    MAE (Ortalama Mutlak Hata)
    MSE (Ortalama Kare Hata)

✅ Bu sayede basit ve çoklu modelin performansı karşılaştırıldı.




-------------------------*Sınıflandırma Modeli: DiabetesKnnClassifier Sınıfı-------------------------
Öncelikle KNN algoritmasını anlayalım:
Örnek:
170	60	Zayıf
165	70	Normal
180	75	Normal
175	90	Kilolu
172 78    ?   (Yeni veri geldi.)

Bu kişi için KNN şunu yapar:
1-) Bu yeni kişinin her veri noktasına mesafesini ölçer (mesela Öklid mesafesi)
2-) En yakın K veri noktasını bulur (örneğin K=3)
3-) Komşuların sınıfı: Normal, Normal, Kilolu → Çoğunluk: Normal
4-) Yeni kişiyi Normal olarak tahmin eder


-Bu sınıfın amacı, load_diabetes() veri setini kullanarak:
-Sürekli target değerini sınıflara dönüştürmek (örneğin düşük, orta, yüksek)
-Ve bu sınıflara göre KNN algoritması ile sınıflandırma yapmak. -> K-Nearest Neighbors-> K-En Yakın Komşu

load_diabetes() veri seti regresyon odaklı olduğu için, target sayısaldı.
Denetimli Öğrenme Kapsamında Sınıflandırma Modeli kurmamız gerekiyordu.
Bu yüzden: 
➡️ Sayısal hedef değişkeni kategorilere böldük
➡️ Böylece KNN gibi sınıflandırma algoritması kullanılabilir hale geldi.


✳️ __init__(self, k=5, n_bins=3)
Sınıf başlatıldığında:
    -Kaç komşuya bakılacağını (k)
    -Kaç sınıf (kategori) oluşturulacağını (n_bins)
    -KNN sınıflandırıcı modelini oluşturur (KNeighborsClassifier)

    ➡️Modelin temel parametreleri burada tanımlanır.

✳️ load_and_prepare_data(self)
Veri setini hazırlar ve sınıflandırma için uygun hale getirir:
    -load_diabetes() veri setini yükler
    -y hedef değişkenini 3 sınıfa ayırır: düşük, orta, yüksek
    -train_test_split() ile veriyi eğitim ve test olarak böler

    ➡️ Modelin eğitilebilmesi için gereken tüm veriler hazır olur

✳️ train(self)
Amaç:
    -Modeli eğitim verisi ile "eğitir" (veriyi ezberletir).
    -self.X_train ve self.y_train ile fit() çağrılır
    
    ➡️KNN tembel öğrenici olduğu için aslında verileri saklar, öğrenme işlemi tahminde yapılır.


✳️ evaluate(self) -> Degerlendirmek, ölçmek.
Modelin başarısını test verisi ile ölçer ve sonuçları görselleştirir:

    -predict() ile tahmin yapar
    -accuracy_score ile genel başarıyı ölçer
    -classification_report ile her sınıf için precision, recall, f1-score verir
    -confusion_matrix ile hata ve doğru tahminleri ısı haritası (heatmap) ile görselleştirir

    ➡️Bu fonksiyon modelin ne kadar iyi çalıştığını anlamamızı sağlar.

--------------------------**Kısaca Bazı Bilgiler Silsilesi**: ------------------------

R² Skoru(Determination Coefficient):
    Modelin hedef değişkeni ne kadar açıkladığını gösterir.
    0 ile 1 arasında değer alır.
    1.0	Mükemmel model (tüm varyansı açıklıyor)
    0.6–0.8	Güçlü model
    0.3–0.5	Orta seviye model
    < 0.3	Zayıf model

Mean Absolute Error(MAE):
    Ortalama tahmin hatası (birim cinsinden)
    Ne kadar küçükse o kadar iyi
    MAE= (1/n) * ∑∣ygercek − ytahmin∣

Mean Squared Error(MSE):
    Hataların karesi alınarak ortalaması bulunur.
    Büyük hataları cezalandırır (MAE’ye göre daha katıdır)
    Sıfıra ne kadar yakınsa o kadar iyi
    (1/n) * ∑[(ygercek − ytahmin)^2]

Accuracy (Doğruluk) [Sınıflandırmada]:
    Kaç tahminin doğru olduğunu gösterir.
    Acc = (Dogru Tahmin Sayısı)/(Toplam Tahmin Sayısı)

F1-score (özellikle Macro F1):
    Precision (isabetlilik) ve Recall (duyarlılık) dengesini alır
    F1 = 2 * (Precision*Recall)/(Precision+Recall)
​    0 ile 1 arasında bir deger alır. 1'e ne kadar yakınsa o kadar iyidir.

Precision – (Kesinlik / İsabet Oranı):
    Modelin tahmin ettiği pozitiflerden kaçı gerçekten pozitif?
    Precision = (True Positive) / (True Pos. + False Pos.)
    Yüksek Precision Ne Demek?

    Model "Bu sınıfa ait!" dediğinde gerçekten o sınıfa ait olma ihtimali yüksek.
    Yani model "çok seçici" davranıyor.
    Yanlış alarmları azaltıyor.

    Model 10 kişiye "COVID pozitif" dedi.
    Bunların 8’i gerçekten pozitifti → Precision = 8 / 10 = 0.80

Recall – (Duyarlılık / Yakalama Oranı):
    Gerçek pozitiflerin ne kadarını bulabildin?
    Recall = (True Positive) / (True Pos. + False Negative.)

Support:
    Her sınıfa ait kaç örnek olduğunu gösterir.




-------------------------*Regresyon Sonucları: ----------------------------------

Basit Regresyon (bmi)
R² Skoru: 0.2334
MAE: 52.26
MSE: 4061.83

Çoklu Regresyon
R² Skoru: 0.4526
MAE: 42.79
MSE: 2900.19

-------------------------*Sonuclar: k = 5 Degeri Icin Sonuclar--------------------------
KNN (k=5) sınıflandırma modeli eğitildi.
KNN Sınıflandırma Değerlendirmesi
Doğruluk (Accuracy): 0.5506

Sınıflandırma Raporu:
               precision    recall  f1-score   support

           0       0.61      0.68      0.64        34
           1       0.43      0.54      0.48        28
           2       0.69      0.41      0.51        27

    accuracy                           0.55        89
   macro avg       0.57      0.54      0.54        89
weighted avg       0.57      0.55      0.55        89

-------------------------* Genel Sonuclar: k =3,5,7,9 Degeri Icin Sonuclar--------------------------

K	Accuracy	Macro F1	Düşük R.   Orta R.	 Yüksek R.	Not
3	 0.5281	      0.51	      0.68	    0.54	   0.33	    Güçlü precision, ama Yüksek sınıf recall düşük
5	 0.5506	      0.54	      0.68	    0.54	   0.41	    EN DENGELİ model
7	 0.5169	      0.50	      0.71	    0.43	   0.37	    En zayıf genel başarı
9	 0.5506	      0.53	      0.76	    0.43	   0.41	    Düşük sınıfta en iyi ama Orta karışık


-------------------------*Standartlaştırma Modeli: StandardScalerHandler Sınıfı-------------------------

KNN (k-En Yakın Komşu) gibi mesafe tabanlı algoritmalar, verideki özelliklerin büyüklüğünden etkilenir.
Her özelligi aynı hale getirmek için bu sınıfı olusturduk.

z = (x−μ) / σ

-​μ (mean)-> Ortalama
-σ (std)-> Standart sapma
-Her sütun → ortalaması 0, standart sapması 1 olacak şekilde dönüştürülür

Faydaları:
-Mesafe hesaplaması daha adil olur
-Daha iyi sınıflandırma sonuçları verir
-Accuracy ve F1-score yükselebilir.


-------------------------*Logistic Regression Modeli: DiabetesLogisticClassifier Sınıfı-------------------------
-------------------------*Logistic Regression Sonucları: ----------------------------------

Logistic Regression modeli eğitildi.
Logistic Regression Değerlendirmesi

Doğruluk (Accuracy): 0.5843

Sınıflandırma Raporu:
               precision    recall  f1-score   support

           0       0.68      0.74      0.70        34
           1       0.42      0.36      0.38        28
           2       0.61      0.63      0.62        27

    accuracy                           0.58        89
   macro avg       0.57      0.57      0.57        89
weighted avg       0.57      0.58      0.58        89




-------------------------* Genel Sonuclar: Algoritmaların Karşılaştırılması--------------------------

Metrik	                    KNN (k=5)	       Logistic Regression

Accuracy       	             0.5506	                 0.5843
Macro F1-score	             0.54	                  0.57
Weighted F1-score	         0.55	                  0.58
En güçlü sınıf	             Sınıf 0 (Düşük)	    Sınıf 0 & 2
En zayıf sınıf	             Sınıf 2	             Sınıf 1



