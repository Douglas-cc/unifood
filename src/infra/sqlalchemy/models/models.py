from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base
from sqlalchemy import (
    Integer,
    Column,
    String,
    Float,
    Boolean,
    ForeignKey
)

'''
back populations Serve para preencher por exemplo 
se eu desejo prrencher algo de produto em usuario.
'''

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    telephone = Column(String)
    password = Column(String)

    products = relationship('Product', back_populates='user')
    my_user = relationship('Purchase', back_populates='user')
    
class Product(Base):
    __tablename__ = 'product'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    available = Column(Boolean)    
    size = Column(String)
    user_id = Column(Integer, ForeignKey('user.id', name='fk_user'))
    
    user = relationship('User', back_populates='products')
    
class Purchase(Base):
    __tablename__ = 'purchase'
    
    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)
    delivery_location = Column(String)  
    delivery_type = Column(String)
    description = Column(String)
    
    user_id = Column(Integer, ForeignKey('user.id', name='fk_purchase_user'))
    product_id = Column(Integer, ForeignKey('product.id', name='fk_purchase_product'))
    
    user = relationship('User', backref='purchase')
    product = relationship('Product')