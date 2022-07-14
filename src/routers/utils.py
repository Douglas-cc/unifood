from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import token_provider 
from src.infra.sqlalchemy.repositories.user import RepositorieUser
from jose import JWTError

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

def get_user_on(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    exeception = HTTPException(status_code=401,detail='invalid token')
    try:
        telephone = token_provider.verify_access_token(token)
    except JWTError:
       raise exeception
    
    if not telephone:
        raise exeception
    
    user = RepositorieUser(db).search_user(telephone)
    if not user:
        raise exeception    
    return user


def get_sales_user(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    exeception = HTTPException(status_code=401,detail='invalid token')


def delete_user(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    exeception = HTTPException(status_code=401, detail='invalid token')
    try:
        telephone = token_provider.verify_access_token(token)
    except JWTError:
       raise exeception
   
    if not telephone:
        raise exeception
    
    RepositorieUser(db).delete_user(telephone)
    return 'User deleted!' 
