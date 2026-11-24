# Hello API

My first FastAPI project, built on WSL (Ubuntu).

## Run it
pip install -r requirements.txt
uvicorn apphi:myapi --reload

Then open http://localhost:8000/docs

![tests](https://github.com/bsumanath/hello-api/actions/workflows/tests.yml/badge.svg)


# Iris Classifier API

A machine learning API that predicts iris flower species from 4 measurements.
Built with **scikit-learn** (Random Forest) and served with **FastAPI** on WSL (Ubuntu).

## Model
- Algorithm: Random Forest (100 trees)
- Dataset: Iris (150 samples, 3 classes)
- Test accuracy: ~96.7% (20% hold-out set)

## Run it
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python train.py              # trains and saves model.joblib
uvicorn apphi:myapi --reload
```
Open http://localhost:8000/docs

## Example
POST /predict
```json
{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}
```
Response:
```json
{"species": "setosa", "confidence": 1.0, "probabilities": {"setosa": 1.0, "versicolor": 0.0, "virginica": 0.0}}
```

## Run with Docker
```bash
docker build -t iris-api .
docker run -p 8000:8000 iris-api
```
Open http://localhost:8000/docs





