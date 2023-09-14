from typing import List

from fastapi import FastAPI

from model import Service

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/services")
async def create_services(services: List[Service]):


