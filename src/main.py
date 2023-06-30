from fastapi import FastAPI

from src.router import initialize_routes

from middlewares.startup import on_start

app = FastAPI()

on_start(app)

initialize_routes(app)
