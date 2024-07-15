from fastapi import FastAPI
from app.routes.app import router as app_router
app = FastAPI()

app.include_router(app_router, prefix="/app")

