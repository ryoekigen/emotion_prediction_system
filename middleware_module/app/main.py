from fastapi import FastAPI
from app import routes

app = FastAPI(title="Middleware Module")

app.include_router(routes.router)
