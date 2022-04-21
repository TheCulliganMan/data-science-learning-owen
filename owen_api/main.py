from typing import List

import redis
from fastapi import FastAPI
from pandera.typing import DataFrame

from .model import xgboost_model
from .schema import PredictSchema

r = redis.Redis(
    host="redis",
    decode_responses=True,
)

app = FastAPI()


@app.get("/")
def hello_world():
    r.incr("counter")
    counter = r.get("counter")
    return {"message": f"Hello World! {counter}"}


@app.get("/owen")
def hello_owen():
    return {"message": "Hello Owen!"}


@app.post("/predict/", response_model=List[int])
def predict(transactions: DataFrame[PredictSchema]):
    predictions = xgboost_model.predict(transactions).tolist()
    return predictions


if __name__ == "__main__":
    print(hello_world())
