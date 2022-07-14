from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import product, auth, purchase
from src.infra.sqlalchemy.config.database import create_db

create_db()
app = FastAPI()


@app.get('/')
def list_purchases():
    return {'Bem vindo'}


origins = ['http://127.0.0.1:8000/']

# CORS
app.add_middleware(
  CORSMiddleware, 
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*']
)

# rotas produtos
app.include_router(product.router)

# rotas de autenticação e autorização
app.include_router(auth.router, prefix='/auth')

# rotas de pedidos 
app.include_router(purchase.router)