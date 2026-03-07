from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.api.base import router as base_router
from src.api.locations import router as locations_router
from src.api.users import router as users_router


def create_app() -> FastAPI:
    app = FastAPI(root_path="/api/v1")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(base_router, prefix="/base", tags=["Base APIs"])
    app.include_router(locations_router, prefix="/blog", tags=["Blog"])
    app.include_router(users_router, prefix="/blog", tags=["Blog"])

    return app