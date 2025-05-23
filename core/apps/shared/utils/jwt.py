from typing import Dict, Optional
from config.env import env
import jwt
from datetime import datetime, timedelta

def get_claim(token: str) -> Optional[Dict]:
    if token is not None:
        try:
            claim = jwt.decode(token, env.str("DJANGO_SECRET_KEY"), algorithms=["HS256"])
            return claim
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
    return None


def get_pk(request) -> Optional[int]:
    token = request.headers.get("token", None)
    print("TOKEN:", token)

    if token is None:
        return None  

    claim = get_claim(token)

    if claim is None:
        return None  

    user_id = claim.get("user_id")
    return user_id  
