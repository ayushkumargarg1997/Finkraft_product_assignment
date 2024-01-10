from fastapi import FastAPI, Body, Depends, APIRouter, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.auth.auth import AuthHandler

auth_router = APIRouter()
auth_handler = AuthHandler()
security = HTTPBearer()

async def auth_wrapper(auth: HTTPAuthorizationCredentials = Security(security)):
    req = await authenticate_token(auth.credentials)
    return req


async def authenticate_token(token):

    res = auth_handler.decode_token(token)
    if not res:
        raise HTTPException(status_code=401, detail="Token is invalid")
        
    return res

