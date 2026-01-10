from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.sintomasAPI import router as sintomas_router

app = FastAPI(
    title="HealthIA API",
    description="API para predição de diagnósticos médicos com base em sintomas.",
    version="1.0.0"
)

# CORS liberado (necessário para Netlify / frontend externo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # depois você pode restringir para o domínio do Netlify
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas da API
app.include_router(sintomas_router, tags=["Sintomas"])
