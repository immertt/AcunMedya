from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import pandas as pd

class DiabetesRegressor:
    def __init__(self):
        self.data = load_diabetes()
        self.X = pd.DataFrame(self.data.data, columns=self.data.feature_names)
        self.y = self.data.target

    def train_simple_model(self, feature_name):
        X_simple = self.X[[feature_name]]
        X_train, X_test, y_train, y_test = train_test_split(X_simple, self.y, test_size=0.2, random_state=42)

        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        self.print_metrics(f"Basit Regresyon ({feature_name})", y_test, y_pred)

    def train_multiple_model(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        self.print_metrics("Çoklu Regresyon", y_test, y_pred)

    def print_metrics(self, model_name, y_true, y_pred):
        print(f"\n{model_name}")
        print("R² Skoru:", round(r2_score(y_true, y_pred), 4))
        print("MAE:", round(mean_absolute_error(y_true, y_pred), 2))
        print("MSE:", round(mean_squared_error(y_true, y_pred), 2))
