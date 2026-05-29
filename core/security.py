from passlib.context import CryptContext


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str) -> str: #convierte la contraseña en algo como:$2b$12$K9...
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:#sirve para comprobar si la contraseña escrita coincide con el hash guardado.
    return pwd_context.verify(plain_password, hashed_password)