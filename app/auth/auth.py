import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
import hashlib


class AuthHandler():
    security = HTTPBearer()
    # pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    load_dotenv()
    secret = os.getenv('jwt_secret')
    algorithm = os.getenv('jwt_algorithm')

    def get_password_hash(self, password):
        # Use hashlib library for basic password hashing
        sha256 = hashlib.sha256()
        sha256.update(password.encode('utf-8'))
        return sha256.hexdigest()

    def verify_password(self, plain_password, hashed_password):
        # Simplified password verification
        return hashed_password == self.get_password_hash(plain_password)

    def encode_token(self, user_id):
        # Generate JWT token
        payload = {
            'exp': datetime.utcnow() + timedelta(days=30, minutes=0),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(payload, self.secret, self.algorithm)

    def decode_token(self, token):
        try:
            # Decode JWT token
            payload = jwt.decode(token, self.secret, self.algorithm)
            return payload
        except jwt.ExpiredSignatureError:
            return False
        except jwt.InvalidTokenError:
            return False

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        # Wrapper for decoding token from HTTP Authorization header
        return self.decode_token(auth.credentials)
