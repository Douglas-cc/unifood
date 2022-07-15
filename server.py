from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from src.routers import product, auth, purchase
from src.infra.sqlalchemy.config.database import create_db
from src.middlewares.timer import time_request
from src.jobs.write_notification import send_notification

create_db()
app = FastAPI()


@app.get('/')
def list_purchases():
    return {'Bem vindo'}


@app.post('/send-notification/{email}')
async def send_email(email: str, background: BackgroundTasks):
  background.add_task(
    send_notification,
    email, 
    'Tudo joia?'
  )
  return {'Message': 'Email enviado em background!'}

origins = ['http://127.0.0.1:8000/']

# CORS
app.add_middleware(
  CORSMiddleware, 
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*']
)

# time middleware
app.add_middleware(BaseHTTPMiddleware, dispatch=time_request)

# rotas produtos
app.include_router(product.router)

# rotas de autenticação e autorização
app.include_router(auth.router, prefix='/auth')

# rotas de pedidos 
app.include_router(purchase.router)