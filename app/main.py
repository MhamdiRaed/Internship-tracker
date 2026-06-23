from fastapi import FastAPI
from app.api import internships

app = FastAPI()

app.include_router(internships.router)

@app.get("/")
def root():
    return {"status": "ok"}