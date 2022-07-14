from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from src.schemas.schemas import Product, ProductSimple
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.product import RepositorieProduct


router = APIRouter()

@router.post('/products', status_code=201)
def create_product(product: Product, db: Session = Depends(get_db)):
    return RepositorieProduct(db).create_product(product)


@router.get("/products/{id}")
def search_product(id: int, db: Session = Depends(get_db)):
    located_product = RepositorieProduct(db).search_product(id)
    if not located_product:
        raise HTTPException(status_code = 404, detail='Product does not exist')
    return located_product

    
@router.get('/products', response_model=List[Product])
def list_products(db: Session = Depends(get_db)):
    return RepositorieProduct(db).ready_product()


@router.put('/products/{id}/update', response_model=ProductSimple)
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    RepositorieProduct(db).update_product(id, product)
    product.id = id
    return product


@router.delete('/products/{id}/delete')
def delete_product(id: int, db: Session = Depends(get_db)):
    RepositorieProduct(db).delete_product(id)
    return 'Product deleted'