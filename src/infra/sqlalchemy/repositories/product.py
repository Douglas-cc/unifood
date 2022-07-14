from sqlalchemy.orm import Session
from sqlalchemy import update, delete, select
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorieProduct():
    def __init__(self, db: Session):
       self.db = db 
       
    def create_product(self, product: schemas.Product):
        query = models.Product(
            name = product.name,
            description = product.description,
            price = product.price,
            available = product.available,
            user_id = product.user_id,
            size = product.size
        )
        self.db.add(query)
        self.db.commit()
        self.db.refresh(query)
        return query
    
    def ready_product(self):
        query = select(models.Product)
        return self.db.execute(query).scalars().all()
    
    
    def update_product(self, id: int, product: schemas.Product):
        query = update(models.Product).where(
            models.Product.id == id).values(
                name = product.name,
                description = product.description,
                price = product.price,
                available = product.available,
                size = product.size
            )
        self.db.execute(query)
        self.db.commit()
    
    
    def delete_product(self, id: int):
        query = delete(models.Product).where(
            models.Product.id == id
        )
        self.db.execute(query)
        self.db.commit()
    
    
    def search_product(self, id: int):
        query = select(models.Product).where(
            models.Product.id == id
        )
        return self.db.execute(query).scalars().all() 
        
       