from fastapi import Depends
from fastapi.exceptions import HTTPException
from fastapi.security import HTTPBearer

from .utils import VerifyToken

# Scheme for the Authorization header
tokenAuthScheme = HTTPBearer()


class token:
    credentials: str


def has_access(token: str = Depends(tokenAuthScheme)):

    result = VerifyToken(token.credentials).verify()

    if result.get("status"):
        # response.status_code = status.HTTP_400_BAD_REQUEST
        raise HTTPException(401, result.get("message"))
