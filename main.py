from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

from model import convert, predict

app = FastAPI()


# pydantic models


class StockIn(BaseModel):
    ticker: str


class StockOut(StockIn):
    forecast: dict

class Item(BaseModel):
    ticker: str

# routes

@app.post("/predict")
async def get_prediction(payload: StockIn):
    ticker = payload.ticker

    prediction_list = predict(ticker)

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {"ticker": ticker, "forecast": convert(prediction_list)}
    return return templates.TemplateResponse("item.html", response_object)

@app.get("/ping")
async def pong():
    return {"ping": "pong!"}
