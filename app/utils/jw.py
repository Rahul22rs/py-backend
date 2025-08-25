from fastapi import Request, HTTPException, Depends
from fastapi.responses import JSONResponse
from .JwtUtils import JwtUtils

jwtUtils = JwtUtils()


async def verify_jwt(request: Request):
    token = request.headers.get("Authorization")
    if token is None:
        token = ""
    decoded_token = jwtUtils.get_decoded_token(token=token)
    if decoded_token is None:
        raise HTTPException(status_code=403, detail="Invalid Authorization")
    request.state.decoded_token=decoded_token
