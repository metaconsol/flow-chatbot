from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import PlainTextResponse
from config import VERIFY_TOKEN
from webhook import process_webhook


# -------- RAG IMPORTS -------- #
from rag import initialize_vector_db, get_context
from agent import generate_response

# -------- RAG INIT -------- #
vector_db = initialize_vector_db()


app = FastAPI()

@app.get("/webhook")
def verify(mode: str = None, token: str = None, challenge: str = None):
    if token == VERIFY_TOKEN:
        return PlainTextResponse(challenge)
    return PlainTextResponse("Error")

@app.post("/webhook")
async def webhook(request: Request, background_tasks: BackgroundTasks):
    data = await request.json()

    try:
        await process_webhook(data, background_tasks)
    except Exception as e:
        print("Error:", e)

    return {"status": "ok"}