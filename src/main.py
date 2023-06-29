from fastapi import FastAPI

from src.router import initialize_routes

app = FastAPI()

initialize_routes(app)
