from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


#Veri setini temizleme hazırlama
class DataPreprocessor:
    def __init__(self, path):
        self.df = pd.read_csv(path)
        self.label_encoder = LabelEncoder()

    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r"http\S+", "", text)
        text = re.sub(r"@\w+", "", text)
        text = re.sub(r"[^a-zA-Z\s]", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text

    def prepare(self):
        self.df = self.df[['text', 'airline_sentiment']]
        self.df['text_clean'] = self.df['text'].apply(self.clean_text)
        self.df['label'] = self.label_encoder.fit_transform(self.df['airline_sentiment'])

        X = self.df['text_clean']
        y = self.df['label']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        return self.X_train, self.X_test, self.y_train, self.y_test, self.label_encoder

#Duygu Analizi Modeli
#Modeli oluşturma ve eğitme
class SentimentModel:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=5000)
        self.model = LogisticRegression(max_iter=1000)

    def train(self, X_train, y_train):
        self.X_train_vec = self.vectorizer.fit_transform(X_train)
        self.model.fit(self.X_train_vec, y_train)

    def transform_test_data(self, X_test):
        return self.vectorizer.transform(X_test)

    def predict(self, X_test_vec):
        return self.model.predict(X_test_vec)

#Değerlendirme Fonksiyonu
#Modelin doğruluğunu ve sınıflandırma raporunu gösterme
#Karışıklık matrisini gösterme
def evaluate_model(y_true, y_pred, label_encoder):
    acc = accuracy_score(y_true, y_pred)
    print("✅ Doğruluk (Accuracy):", round(acc, 4))

    print("\n📋 Sınıflandırma Raporu:")
    print(classification_report(y_true, y_pred, target_names=label_encoder.classes_))

    # Karışıklık matrisi
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(6,4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=label_encoder.classes_,
                yticklabels=label_encoder.classes_)
    plt.title("🔍 Karışıklık Matrisi")
    plt.xlabel("Tahmin Edilen")
    plt.ylabel("Gerçek")
    plt.tight_layout()
    plt.show()


def main():
    preprocessor = DataPreprocessor("D:\\AcunMedya\\AcunMedya\\Python_Ile_Veri_Bilimi_Nisan_2_Hafta_Odevi\\Tweets.csv")
    X_train, X_test, y_train, y_test, label_encoder = preprocessor.prepare()

    sentiment_model = SentimentModel()
    sentiment_model.train(X_train, y_train)

    X_test_vec = sentiment_model.transform_test_data(X_test)
    y_pred = sentiment_model.predict(X_test_vec)

    evaluate_model(y_test, y_pred, label_encoder)


if __name__ == "__main__":
    main()
