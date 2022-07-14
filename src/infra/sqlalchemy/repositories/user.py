from sqlalchemy.orm import Session
from sqlalchemy import update, delete, select
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorieUser:
    def __init__(self, db: Session):
       self.db = db 
       
    def create_user(self, user: schemas.User):
        query = models.User(
            name = user.name,
            telephone = user.telephone,
            password = user.password
        )
        self.db.add(query)
        self.db.commit()
        self.db.refresh(query)    
        return query
    
    
    def ready_users(self):
        query = select(models.User)
        return self.db.execute(query).scalars().all()
    
    
    def update_user(self, id: int, user: schemas.User):
        query = update(models.User).where(
            models.User.id == id).values(
                name = user.name,
                telephone = user.telephone,
                password = user.password
            )
        self.db.execute(query)
        self.db.commit()
    
    
    def delete_user(self, telephone: str):
        query = delete(models.User).where(
            models.User.telephone == telephone
        )
        self.db.execute(query)
        self.db.commit()     
        
        
    def search_user(self, telephone: str) -> models.User:
        query = select(models.User).where(
            models.User.telephone == telephone
        )
        return self.db.execute(query).scalars().first() 
        
       