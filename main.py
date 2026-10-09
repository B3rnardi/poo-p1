from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.marmita_routes import router as marmita_router
from app.routes.cliente_routes import router as cliente_router
from app.routes.pedido_routes import router as pedido_router

app = FastAPI(title='MarmitaFit API', version='1.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(marmita_router)
app.include_router(cliente_router)
app.include_router(pedido_router)

@app.get('/')
def raiz():
    return {'api': 'MarmitaFit', 'docs': '/docs'}
