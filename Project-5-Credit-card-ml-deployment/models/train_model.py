# Импорт библиотек
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib
import os

df = pd.read_csv("data/UCI_Credit_Card.csv")
print(df.head())

# 2. Готовим признаки (X) и целевую переменную (y)
# Целевая переменная (дефолт) находится в последнем столбце
X = df.drop(columns=['ID', 'default.payment.next.month'])
y = df['default.payment.next.month']

# 3. Разделяем на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Создаем пайплайн: сначала масштабируем данные, потом обучаем классификатор
# Пайплайн очень удобен, так как он сохранит ВСЮ цепочку преобразований [citation:4]
model = Pipeline([
    ('scaler', StandardScaler()),        # Нормализуем признаки
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42)) # Обучаем лес
])

# 5. Обучаем модель
print("Обучение модели...")
model.fit(X_train, y_train)

# 6. Сохраняем модель в папку models/
os.makedirs('models', exist_ok=True)
model_path = 'models/model_v1.pkl'
joblib.dump(model, model_path)
print(f"Модель сохранена в {model_path}")

# Небольшая проверка, что всё работает
accuracy = model.score(X_test, y_test)
print(f"Точность на тестовых данных: {accuracy:.2f}")