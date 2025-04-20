from DiabetesRegressor import DiabetesRegressor
from DiabetesKnnClassifier import DiabetesKnnClassifier

def main():
    # 1️ Lineer Regresyon
    reg = DiabetesRegressor()
    reg.train_simple_model("bmi")
    reg.train_multiple_model()

    # 2️ KNN Sınıflandırma
    knn = DiabetesKnnClassifier(k=5)
    knn.load_and_prepare_data()
    knn.train()
    knn.evaluate()

if __name__ == "__main__":
    main()
