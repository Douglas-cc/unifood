from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from src.schemas.schemas import Purchase, User
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.purchase import RepositoriePurchase
from src.routers.auth import  get_user_on

router = APIRouter()

@router.post('/purchase', status_code=201)
def create_purchase(purchase: Purchase, db: Session = Depends(get_db)):
    return RepositoriePurchase(db).create_purchase(purchase)


@router.get('/purchase', response_model=List[Purchase])
def list_purchases(user: User = Depends(get_user_on), db: Session = Depends(get_db)):
    return RepositoriePurchase(db).list_sales_user_id(user.id)