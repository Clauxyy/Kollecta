from fastapi import FastAPI

app = FastAPI(
    title="Kollecta API",
    description="API pentru platforma Kollecta",
    version="0.1.0",
)

@app.get("/")
def home():
    return {"message": "Kollecta API functioneaza!"}

@app.get("/health")
def health():
    return {"status": "ok"}
