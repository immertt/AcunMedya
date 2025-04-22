from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from StandardScalerHandler import StandardScalerHandler
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class DiabetesLogisticClassifier:
    def __init__(self, n_bins=3):
        self.n_bins = n_bins #Target degiskeni 3 sinifa ayrılacak.
        self.model = LogisticRegression(max_iter=1000, solver="lbfgs")  
        #Model öğrenemezse durması için maksimum 1000 tekrar yapacak.
        #lbfgs, L2 regularization kullanır ve çok sınıflı sınıflandırma için optimizasyon algoritmasıdır.
        #L2 regularization, modelin aşırı öğrenmesini önlemek için kullanılır.

    def load_and_prepare_data(self):
        data = load_diabetes()
        X = pd.DataFrame(data.data, columns=data.feature_names)
        y = data.target

        discretizer = KBinsDiscretizer(n_bins=self.n_bins, encode="ordinal", strategy="quantile")
        y_binned = discretizer.fit_transform(y.reshape(-1, 1)).astype(int).ravel()

        scaler = StandardScalerHandler()
        X_scaled = scaler.fit_transform(X)

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X_scaled, y_binned, test_size=0.2, random_state=42
        )

    def train(self):
        self.model.fit(self.X_train, self.y_train)
        print("Logistic Regression modeli eğitildi.")

    def evaluate(self):
        y_pred = self.model.predict(self.X_test)
        acc = accuracy_score(self.y_test, y_pred)

        print("\nLogistic Regression Değerlendirmesi")
        print("Doğruluk (Accuracy):", round(acc, 4))
        print("\nSınıflandırma Raporu:\n", classification_report(self.y_test, y_pred))

        cm = confusion_matrix(self.y_test, y_pred, normalize="true")
        sns.heatmap(cm, annot=True, cmap="Greens",
                    xticklabels=["Düşük", "Orta", "Yüksek"],
                    yticklabels=["Düşük", "Orta", "Yüksek"])
        plt.title("Logistic Regression – Karışıklık Matrisi")
        plt.xlabel("Tahmin Edilen")
        plt.ylabel("Gerçek")
        plt.tight_layout()
        plt.show()
