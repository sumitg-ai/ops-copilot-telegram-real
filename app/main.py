from fastapi import FastAPI, Request
from .telegram_router import handle_update

app = FastAPI()

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

@app.post("/telegram/webhook")
async def telegram_webhook(request: Request):
    payload = await request.json()
    text = await handle_update(payload)
    return {"ok": True, "message": text}
