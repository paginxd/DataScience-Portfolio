# app/api.py
from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)
model = None

FEATURES = [
    'LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE',
    'PAY_0', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6',
    'BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6',
    'PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6'
]


def load_model():
    global model
    # Ищем модель в папке models (на уровень выше)
    model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'model_v1.pkl')
    
    if not os.path.exists(model_path):
        raise Exception(f"Модель не найдена по пути {model_path}")
    
    model = joblib.load(model_path)
    print("Модель успешно загружена!")
    return True

@app.route('/health', methods=['GET'])
def health_check():
    return {'status': 'ok', 'message': 'Service is running'}, 200

@app.route('/predict', methods=['POST'])
def predict():
    global model
    
    if model is None:
        load_model()
    
    try:
        data = request.get_json()
        missing_features = [f for f in FEATURES if f not in data]
        if missing_features:
            return {
                'error': f"Отсутствуют признаки: {missing_features}",
                'required_features': FEATURES
            }, 400
            
        input_data = {feature:data[feature] for feature in FEATURES}
        input_df = pd.DataFrame([input_data])
        
        probability = model.predict_proba(input_df)[0][1]
        prediction = model.predict(input_df)[0]
        
        return {
            'prediction': int(prediction),
            'probability_default': round(float(probability), 4),
            'model_version': 'v1'
        }, 200
    except Exception as e:
        return {'error': str(e)}, 400

if __name__ == '__main__':
    load_model()
    print("\n" + "="*50)
    print("Сервис запущен на http://127.0.0.1:5000")
    print("Эндпоинты:")
    print("  GET  /health")
    print("  POST /predict")
    print("="*50 + "\n")
    app.run(host='0.0.0.0', port=5000, debug=False)