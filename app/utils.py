from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt_sha256"], deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)