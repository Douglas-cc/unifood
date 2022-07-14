from pydantic import BaseModel
from typing import Optional, List


class ProductSimple(BaseModel):
    id: Optional[int] = None
    name: str
    price: float
    description: str
    
    class Config:
        orm_mode = True  


class User(BaseModel):
    id: Optional[str] = None
    name: str
    telephone: str
    password: str
    products: List[ProductSimple] = []
    class Config:
        orm_mode = True
 
        
class UserSimple(BaseModel):
    id: Optional[str] = None
    name: str
    telephone: str
    class Config:
        orm_mode = True


class LoginUser(BaseModel):
    password: str
    telephone: str


class LoginSucess(BaseModel):
    user: UserSimple
    access_token: str            
        
                
class Product(BaseModel):
    id: Optional[int] = None
    name: str
    description: str
    price: float
    available: bool = False
    size: str
    
    user_id: Optional[int]
    user: Optional[UserSimple]
    
    class Config:
        orm_mode = True
        
        
class Purchase(BaseModel):
    id: Optional[int] = None
    quantity: str
    delivery_location: str
    delivery_type: str
    description: Optional[str] = 'Sem obervações'

    user_id: Optional[int]
    product_id: Optional[int]
    
    user: Optional[UserSimple]
    product: Optional[ProductSimple]
    
    class Config:
        orm_mode = True