from fastapi import APIRouter

from apps.shortener import controllers

shortener_router = APIRouter()


@shortener_router.get("/")
def test_api_route():
    return controllers.test_api()
