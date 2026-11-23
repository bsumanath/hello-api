from fastapi.testclient import TestClient
from apphi import myapi

client = TestClient(myapi)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    resp = response.json()
    assert resp["status"] == "ok"
    assert resp["message"] == "Welcome to the Iris Classifier API"


def test_predict_setosa():
    flower = {"sepal_length": 5.1, "sepal_width": 3.5,
              "petal_length": 1.4, "petal_width": 0.2}
    response = client.post("/predict", json=flower)
    assert response.status_code == 200
    assert response.json()["species"] == "setosa"


def test_predict_virginica():
    flower = {"sepal_length": 6.7, "sepal_width": 3.0,
              "petal_length": 5.2, "petal_width": 2.3}
    response = client.post("/predict", json=flower)
    assert response.json()["species"] == "virginica"


def test_probabilities_sum_to_one():
    flower = {"sepal_length": 6.0, "sepal_width": 2.9,
              "petal_length": 4.5, "petal_width": 1.5}
    probs = client.post("/predict", json=flower).json()["probabilities"]
    assert abs(sum(probs.values()) - 1.0) < 0.01


def test_negative_value_rejected():
    flower = {"sepal_length": -1, "sepal_width": 3.5,
              "petal_length": 1.4, "petal_width": 0.2}
    response = client.post("/predict", json=flower)
    assert response.status_code == 422


def test_missing_field_rejected():
    flower = {"sepal_length": 5.1, "sepal_width": 3.5}
    response = client.post("/predict", json=flower)
    assert response.status_code == 422
