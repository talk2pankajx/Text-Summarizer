from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from Text_Summarizer.pipeline.prediction import PredictionPipeline

app = FastAPI()

text:str = "waht is text summarization"

@app.get("/",tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training Sucessfullly Completed")
    except Exception as e:
        return Response("Error occurred")
    
@app.post("/predict")
async def predict(text):
    try:
        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        raise e 


if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8080)
    