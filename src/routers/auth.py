from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from src.schemas.schemas import User, UserSimple, LoginUser, LoginSucess
from src.infra.sqlalchemy.config.database import get_db 
from src.infra.sqlalchemy.repositories.user import RepositorieUser
from src.infra.providers import hash_provider, token_provider
from src.routers.utils import get_user_on, delete_user

router = APIRouter()

@router.post('/signup', status_code=201)
def create_user(user: User, db: Session = Depends(get_db)):
    located_user = RepositorieUser(db).search_user(user.telephone)
    if located_user:
        raise HTTPException(
            status_code=400, 
            detail='User already exists with telephone'
        )
    user.password = hash_provider.generate_hash(user.password)
    return RepositorieUser(db).create_user(user)


@router.post('/token', status_code=201, response_model=LoginSucess)
def login(login: LoginUser, db: Session = Depends(get_db)):
    telephone = login.telephone
    password = login.password
    
    exception = HTTPException(status_code=400, 
                              detail='Incorrect phone or password!')
        
    user = RepositorieUser(db).search_user(telephone)
    if not user:
        raise exception
    
    valid_password = hash_provider.verify_hash(password, user.password)
    if not valid_password:
        raise exception
        
    token = token_provider.create_access_token({'sub': user.telephone})
    return LoginSucess(user=user, access_token=token)


@router.get('/me', response_model=UserSimple)            
def me(user: User = Depends(get_user_on), db: Session = Depends(get_db)):
    return user


@router.put('/user/{id}/update')
def update_user(id: int, user: User, db: Session = Depends(get_db)):
    RepositorieUser(db).update_user(id, user)
    return {'Data Update'}


@router.delete('/delete')
def delete_user(user_deleted: User = Depends(delete_user), db: Session = Depends(get_db)):
    return user_deleted