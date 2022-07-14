from sqlalchemy.orm import Session
from sqlalchemy import update, delete, select
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositoriePurchase():
    def __init__(self, db: Session):
        self.db = db
    
    def create_purchase(self, purchase: schemas.Purchase):
        query = models.Purchase(
            quantity = purchase.quantity,
            delivery_location =  purchase.delivery_location,
            delivery_type = purchase.delivery_type,
            description = purchase.description,
            user_id = purchase.user_id,
            product_id = purchase.product_id
        )
        
        self.db.add(query)
        self.db.commit()
        self.db.refresh(query)
        return query       
    

    def list_sales_user_id(self, user_id: int):
        query = select(models.Purchase).where(
            models.Purchase.user_id == user_id
        )
        return self.db.execute(query).scalars().all()
    
    
    def delete_purchase(self, id: int):
        query = delete(models.Purchase).where(
            models.Purchase.id == id
        )
        self.db.execute(query)
        self.db.commit()
    