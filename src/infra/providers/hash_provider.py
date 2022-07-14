from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'])

def generate_hash(secret):
    return pwd_context.hash(secret)


def verify_hash(secret, hash):
    return pwd_context.verify(secret, hash)