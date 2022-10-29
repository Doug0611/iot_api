from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.view import router


app = FastAPI(
    title="API IOT",
    version="0.0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(
    prefix="/api/iot",
    router=router
)

