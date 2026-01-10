from api.sintomasAPI import router as sintomas_router
from fastapi import FastAPI


app = FastAPI(title="HealthIA API", description="API para predição de diagnósticos médicos com base em sintomas.", version="1.0.0")
app.include_router(sintomas_router,  tags=["Sintomas"])


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.sintomasAPI import router as sintomas_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5173",
        "http://localhost:5173",
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sintomas_router)
