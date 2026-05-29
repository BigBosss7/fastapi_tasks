from fastapi import Depends 
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from core.jwt import verify_access_token

security  = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials
    payload = verify_access_token(token)

    if not payload:
        raise HTTPEception(
            status_code=401,
            detail="Token inválido"
        )
    return payload