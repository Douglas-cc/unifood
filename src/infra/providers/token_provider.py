from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = '3123b95f4a2bdd5505402eec22863ddc4d759437'
ALGORITHM = 'HS256' 
EXPIRES_IN_MIN = 3000 


def create_access_token(data: dict):
    data = data.copy()
    expires = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)
    
    data.update({'exp': expires})
    
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)     
    return token


def verify_access_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload.get('sub')