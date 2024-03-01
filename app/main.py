from fastapi import FastAPI
from app.router import router as open_ai_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(open_ai_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
