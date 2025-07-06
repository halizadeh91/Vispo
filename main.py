from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class Poem(BaseModel):
    text: str

@app.post("/analyze")
async def analyze_poem(poem: Poem):
    lines = poem.text.strip().split("\n")
    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    
    # Placeholder for sentiment analysis
    mood = "neutral"
    if any(word in poem.text.lower() for word in ["love", "joy", "sun"]):
        mood = "positive"
    elif any(word in poem.text.lower() for word in ["dark", "death", "cry"]):
        mood = "negative"
    
    return {
        "line_count": line_count,
        "word_count": word_count,
        "mood": mood
    }

@app.get("/")
def read_root():
    return {"message": "Poetry Analyzer API is running"}