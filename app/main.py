from fastapi import FastAPI
from loguru import logger

app = FastAPI()

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed.")
    return {"message": "Welcome to BOLSAPI: the crypto and commodities alert bot API!"}
