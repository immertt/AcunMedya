from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from StandardScalerHandler import StandardScalerHandler
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class DiabetesKnnClassifier:
    def __init__(self, k=5, n_bins=3): # k: komşu sayısı, n_bins: sınıf sayısı(Zayıf, Orta, Şişman) gibi.
        self.k = k
        self.n_bins = n_bins
        self.model = KNeighborsClassifier(n_neighbors=self.k) 
        #scikit-learn'de hazır KNN sınıflandırıcıyı kullanıyoruz.

    def load_and_prepare_data(self):
        # Veriyi yükle
        """
        {
        'data': [...],             # Bağımsız değişkenler (X)
        'target': [...],           # Bağımlı değişken (y)
        'feature_names': [...],    # Sütunların isimleri
        'DESCR': "...",            # Veri seti açıklaması
        'frame': None,
        'data_filename': '...',
        'target_filename': '...'
        }
        """
        data = load_diabetes()
        X = pd.DataFrame(data.data, columns=data.feature_names) # Bağımsız değişkenler
        y = data.target # Bağımlı değişken (target)

        #Problem: y yani target, sürekli bir sayı → KNN sınıflandırma bunu kullanamaz.

        # target'ı sınıflandırma için kategorilere ayır (Düşük, Orta, Yüksek)
        discretizer = KBinsDiscretizer(n_bins=self.n_bins, encode='ordinal', strategy='quantile')
        # 'quantile' stratejisi, veriyi eşit sayıda örnek içeren sınıflara ayırır.
        # 'ordinal' kodlama, her sınıfa bir tamsayı atar (0, 1, 2, ...).
        y_binned = discretizer.fit_transform(y.reshape(-1, 1)).astype(int).ravel()
        # y_binned, y'nin kategorik versiyonudur.
        #fit_transform y degiskenini 2 boyutlu ister, ama modelin y_train olarak kullanabilmesi için tekrar 1D yapmak gerekiyor
        #Artık y_binned → 0, 1, 2 değerleri taşıyan sınıf etiketleri oldu.

        scaler = StandardScalerHandler()
        X_scaled = scaler.fit_transform(X) # Özellikleri ölçeklendir


        # Eğitim ve test setlerine ayır
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X_scaled, y_binned, test_size=0.2, random_state=42
        )


    #KNN modeli aslında klasik anlamda bir şey "öğrenmez",veriyi memorizler.(lazy learner (tembel öğrenici))
    #"Verileri bir kenara kaydediyorum, tahmin zamanı gelince bunlara bakacağım" demektir.
    def train(self):
        self.model.fit(self.X_train, self.y_train)
        print(f"KNN (k={self.k}) sınıflandırma modeli eğitildi.")

    def evaluate(self):
        #Test verileri için sınıf tahminleri yaparız
        y_pred = self.model.predict(self.X_test)
        #Tahminlerin ne kadar doğru olduğunu ölçeriz (dogru tahmin)/(toplam tahmin)
        acc = accuracy_score(self.y_test, y_pred)

        print("\nKNN Sınıflandırma Değerlendirmesi")
        print("Doğruluk (Accuracy):", round(acc, 4))
        print("\nSınıflandırma Raporu:\n", classification_report(self.y_test, y_pred))
        #Her sınıf için precision, recall, f1-score ve support verir
        #precision: "Tahmin ettiğin sınıflar içinde ne kadar doğruydun?"
        #recall: "Gerçek sınıflar içinden ne kadarını doğru buldun?"
        #f1-score: Precision ve Recall’un dengeli halidir.
        #support: Her sınıftan kaç örnek vardı?

        cm = confusion_matrix(self.y_test, y_pred,normalize='true')
        sns.heatmap(cm, annot=True, cmap="Blues", 
                    xticklabels=["Düşük", "Orta", "Yüksek"], 
                    yticklabels=["Düşük", "Orta", "Yüksek"])
        #Satırlar: Gerçek sınıflar
        #Sütunlar: Tahmin edilen sınıflar

        plt.title("KNN Algoritması - Karışıklık Matrisi")
        plt.xlabel("Tahmin Edilen")
        plt.ylabel("Gerçek")
        plt.tight_layout()
        plt.show()
