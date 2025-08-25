from passlib.context import CryptContext
import bcrypt
import os
from datetime import datetime, timedelta, timezone
from typing import Union, Any
from jose import JWTError, jwt


ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = "SECRET"
JWT_REFRESH_SECRET_KEY = "REFRESH"
options = {
    "verify_aud": True,
    "verify_iss": True,
    "aud": "your_audience",
    "iss": "your_issuer",
}


class JwtUtils:
    def str_to_hash(self, input_password: str) -> str:
        # string to BINARY format -> array of bytes
        pwd_bytes = input_password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
        return hashed_password.decode("utf-8")

    def verify_hash(self, plain_password: str, hash_password: str) -> bool:
        password_byte_enc = plain_password.encode("utf-8")
        hashed_byte_enc = hash_password.encode("utf-8")
        return bcrypt.checkpw(
            password=password_byte_enc, hashed_password=hashed_byte_enc
        )

    def create_access_token(
        self, subject: Union[str, Any], expires_delta: int | None = None
    ) -> str:
        if expires_delta is not None:
            expires_delta = datetime.now(timezone.utc).timestamp() + expires_delta  # type: ignore
        else:
            expires_delta = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)  # type: ignore

        to_encode = {"exp": expires_delta, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
        return encoded_jwt

    def create_refresh_token(
        self, subject: Union[str, Any], expires_delta: int | None = None
    ) -> str:
        if expires_delta is not None:
            expires_delta = datetime.now(timezone.utc) + expires_delta  # type: ignore
        else:
            expires_delta = datetime.now(timezone.utc) + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)  # type: ignore

        to_encode = {"exp": expires_delta, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
        return encoded_jwt

    def formateddResponse(self, data=None, message="Success", status=True, errors=None):
        return {
            "status": status,
            "message": message,
            "data": data,
            "errors": errors,
        }

    def get_decoded_token(self, token: str) -> object | None:
        try:
            decoded_token = jwt.decode(
                token, JWT_SECRET_KEY, algorithms=[ALGORITHM], options=options
            )
            print("Token is valid. Payload:", decoded_token)
            return decoded_token
        except JWTError as e:
            print(f"Token validation failed: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
