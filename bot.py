from fastapi import FastAPI, Header, HTTPException, Body
from pydantic import BaseModel
import os

app = FastAPI(title="Cloud Computer Agent API")

BOT_SECRET = os.getenv("BOT_SECRET", "8910286139")

class ChatRequest(BaseModel):
    session_id: str
    message: str
    images: list = []

@app.get("/")
def home():
    return {"status": "success", "message": "KoolBot Backend is Running!"}

@app.post("/chat")
async def chat_endpoint(
    data: ChatRequest, 
    x_api_key: str = Header(None)
):
    if x_api_key != BOT_SECRET:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    # Yahan aapka bot ka logic / playwright agent chalega
    user_message = data.message
    
    return {
        "reply": f"Maine aapka message sun liya: '{user_message}'. Playwright agent is par kaam kar raha hai!",
        "events": []
    }

@app.post("/reset")
async def reset_chat(data: dict = Body(...), x_api_key: str = Header(None)):
    if x_api_key != BOT_SECRET:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return {"status": "reset"}
