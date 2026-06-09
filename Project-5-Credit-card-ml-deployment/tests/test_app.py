import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"


def test_health():
    """Тест проверки здоровья сервиса"""
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_predict():
    """Тест успешного предсказания"""
    data = {
        "LIMIT_BAL": 50000,
        "SEX": 2,
        "EDUCATION": 2,
        "MARRIAGE": 1,
        "AGE": 24,
        "PAY_0": 0,
        "PAY_2": 0,
        "PAY_3": 0,
        "PAY_4": 0,
        "PAY_5": 0,
        "PAY_6": 0,
        "BILL_AMT1": 50000,
        "BILL_AMT2": 50000,
        "BILL_AMT3": 50000,
        "BILL_AMT4": 50000,
        "BILL_AMT5": 50000,
        "BILL_AMT6": 50000,
        "PAY_AMT1": 0,
        "PAY_AMT2": 0,
        "PAY_AMT3": 0,
        "PAY_AMT4": 0,
        "PAY_AMT5": 0,
        "PAY_AMT6": 0
    }
    response = requests.post(f"{BASE_URL}/predict", json=data)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert "probability_default" in response.json()
    assert response.json()["model_version"] == "v1"


def test_predict_missing_fields():
    """Тест: что будет, если отправить не все поля?"""
    data = {"LIMIT_BAL": 50000} 
    
    response = requests.post(f"{BASE_URL}/predict", json=data)
    
    assert response.status_code == 400
    assert "error" in response.json()


def test_predict_invalid_data():
    """Тест: что будет, если отправить невалидные данные?"""
    response = requests.post(f"{BASE_URL}/predict", json="not a json")
    
    assert response.status_code == 400
    assert "error" in response.json()


def test_predict_empty_data():
    """Тест с пустыми данными"""
    response = requests.post(f"{BASE_URL}/predict", json={})
    assert response.status_code == 400
    assert "error" in response.json()


def test_predict_wrong_method():
    """Тест с неправильным HTTP методом"""
    response = requests.get(f"{BASE_URL}/predict")
    assert response.status_code in [400, 405]  # Bad Method или Method Not Allowed