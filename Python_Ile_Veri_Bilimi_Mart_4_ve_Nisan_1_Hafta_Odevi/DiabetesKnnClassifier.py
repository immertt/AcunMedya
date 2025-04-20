from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class DiabetesKnnClassifier:
    def __init__(self, k=5, n_bins=3):
        self.k = k
        self.n_bins = n_bins
        self.model = KNeighborsClassifier(n_neighbors=self.k)

    def load_and_prepare_data(self):
        # Veriyi yükle
        data = load_diabetes()
        X = pd.DataFrame(data.data, columns=data.feature_names)
        y = data.target

        # Sürekli target'ı sınıflandırma için kategorilere ayır (Düşük, Orta, Yüksek)
        discretizer = KBinsDiscretizer(n_bins=self.n_bins, encode='ordinal', strategy='quantile')
        y_binned = discretizer.fit_transform(y.reshape(-1, 1)).astype(int).ravel()

        # Eğitim ve test ayır
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y_binned, test_size=0.2, random_state=42
        )

    def train(self):
        self.model.fit(self.X_train, self.y_train)
        print(f"KNN (k={self.k}) sınıflandırma modeli eğitildi.")

    def evaluate(self):
        y_pred = self.model.predict(self.X_test)
        acc = accuracy_score(self.y_test, y_pred)

        print("\nKNN Sınıflandırma Değerlendirmesi")
        print("Doğruluk (Accuracy):", round(acc, 4))
        print("\nSınıflandırma Raporu:\n", classification_report(self.y_test, y_pred))

        cm = confusion_matrix(self.y_test, y_pred)
        sns.heatmap(cm, annot=True, cmap="Blues", 
                    xticklabels=["Düşük", "Orta", "Yüksek"], 
                    yticklabels=["Düşük", "Orta", "Yüksek"])
        plt.title("Karışıklık Matrisi")
        plt.xlabel("Tahmin Edilen")
        plt.ylabel("Gerçek")
        plt.tight_layout()
        plt.show()
