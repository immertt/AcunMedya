from sklearn.preprocessing import StandardScaler


class StandardScalerHandler:
    def __init__(self):
        self.scaler = StandardScaler()

    def fit_transform(self, X):
        #Verilen X verisini eğitir ve dönüştürülmüş versiyonunu döner
        return self.scaler.fit_transform(X)

    def transform(self, X):
        #Daha önce eğitilmiş ölçekleyici ile yeni veriyi dönüştürür.
        return self.scaler.transform(X)

    def inverse_transform(self, X_scaled):
        #Ölçeklenmiş veriyi orijinal haline geri çevirir.
        return self.scaler.inverse_transform(X_scaled)
