from fastapi import FastAPI

from apps.shortener.apis import shortener_router


def initialize_routes(app: FastAPI):
    app.include_router(
        shortener_router,
        prefix="/shortener",
    )
