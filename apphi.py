
import joblib
from fastapi import FastAPI
from pydantic import BaseModel, Field

myapi = FastAPI(
    title="Beku's Iris Classifier API",
    description="Predicts iris flower species from 4 measurements",
    version="1.0",
)

# Load the trained model once, when the server starts
bundle = joblib.load("model.joblib")
model = bundle["model"]
target_names = bundle["target_names"]


class Numbers(BaseModel):
    a: float
    b: float


class IrisFeatures(BaseModel):
    sepal_length: float = Field(gt=0, description="Sepal length in cm")
    sepal_width: float = Field(gt=0, description="Sepal width in cm")
    petal_length: float = Field(gt=0, description="Petal length in cm")
    petal_width: float = Field(gt=0, description="Petal width in cm")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"sepal_length": 5.1, "sepal_width": 3.5,
                 "petal_length": 1.4, "petal_width": 0.2}
            ]
        }
    }


@myapi.get("/")
def home():
    return {"message": "Iris classifier is running. Go to /docs to try it."}


@myapi.post("/add")
def add_numbers(nums: Numbers):
    return {"a": nums.a, "b": nums.b, "result": nums.a + nums.b}


@myapi.post("/predict")
def predict(features: IrisFeatures):
    row = [[
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width,
    ]]
    pred_index = int(model.predict(row)[0])
    probs = model.predict_proba(row)[0]

    return {
        "species": target_names[pred_index],
        "confidence": round(float(probs[pred_index]), 3),
        "probabilities": {
            name: round(float(p), 3) for name, p in zip(target_names, probs)
        },
    }