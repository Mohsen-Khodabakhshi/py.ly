from fastapi import FastAPI

from src.config import mongo_settings

from services.mongo.connection import MongoConnection


def on_start(app: FastAPI) -> None:
    @app.on_event("startup")
    async def _():
        MongoConnection(
            mongo_settings.host,
            mongo_settings.port,
            mongo_settings.user,
            mongo_settings.password,
        ).get_client()
