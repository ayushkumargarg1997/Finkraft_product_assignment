import re
from fastapi import APIRouter, Depends, HTTPException, Body
from app.db.mongo_connection import get_mongo_connection
import logging
from typing import Optional, List
from app.db.models.user import *
from app.auth.auth_api import *
from app.auth.auth import AuthHandler
from app.user.db_queries import *

user_router = APIRouter()
auth_handler = AuthHandler()

# Set up logging
logging.basicConfig(level=logging.DEBUG, filename="app.log")
logger = logging.getLogger(__name__)

EMAIL_REGEX_PATTERN = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"  # Email regex pattern

def validate_email_format(email):
    if not re.match(EMAIL_REGEX_PATTERN, email):
        raise HTTPException(status_code=400, detail="Invalid email format")

def check_character_limit(value, field_name, limit=100):
    if len(value) > limit:
        raise HTTPException(status_code=400, detail=f"{field_name} exceeds character limit of {limit}")

@user_router.post("/usersignup", response_model=dict)
async def user_signup(user: User_Signup = Body(...)):
    if not user.name or not user.email or not user.password or not user.phone:
        raise HTTPException(status_code=400, detail="Missing details")

    logger.debug(user.email)

    params = (user.email,)

    if await get_userdetail(params):
        raise HTTPException(status_code=400, detail="Email ID already exists. Please choose a different email id")

    try:
        # Check character limits
        check_character_limit(user.name, "Name")
        check_character_limit(user.phone, "Phone")

        # Validate email format
        validate_email_format(user.email)

        # Hash the password
        hash_password = auth_handler.get_password_hash(user.password)

        user_params = (user.name, user.email, hash_password, user.phone)
        userid = await add_user(user_params)

        if not userid:
            raise HTTPException(status_code=400, detail="Failed to add user")

        return {"token": auth_handler.encode_token(userid)}

    except HTTPException as http_error:
        logger.error(f"HTTP Exception: {http_error.detail}")
        raise
    except Exception as e:
        logger.error(f"Error in adding user: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@user_router.post("/userlogin", response_model=dict)
async def user_login(user:User_Login = Body(...)):
    if not user.email or not user.password:
        raise HTTPException(status_code=400, detail="Email and password are required.")

    logger.debug(user.email)

    params = (user.email,)

    user_data = await get_userdetail(params)

    if not user_data or not user_data['id']:
        raise HTTPException(status_code=500, detail="User doesn't exist")

    user_password = user_data['password']

    if user_password == auth_handler.get_password_hash(user.password):
        return {"token": auth_handler.encode_token(user_data['id'])}
    else:
        raise HTTPException(status_code=500, detail="Invalid login details")
