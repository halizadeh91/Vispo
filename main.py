from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import pipeline
import uvicorn

app = FastAPI()
emotion_model = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

class Poem(BaseModel):
    text: str

@app.post("/analyze")
async def analyze(poem: Poem):
    emotions = emotion_model(poem.text)
    top_emotion = sorted(emotions[0], key=lambda x: x['score'], reverse=True)[0]['label'].lower()

    line_count = len(poem.text.strip().splitlines())
    return {"mood": top_emotion, "line_count": line_count}
