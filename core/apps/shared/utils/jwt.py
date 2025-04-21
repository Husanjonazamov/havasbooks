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
    print("TOKEN:", token)  # Tokenni konsolga chiqarish (debug uchun)

    if token is None:
        return None  # Agar token bo'lmasa, None qaytarish

    # Tokenni dekodlash va claimni olish
    claim = get_claim(token)
    print("CLAIM:", claim)  # Claimni konsolga chiqarish (debug uchun)

    if claim is None:
        return None  # Agar claim mavjud bo'lmasa, None qaytarish

    # Yangi: faqat user_id olish
    user_id = claim.get("user_id")
    print("USER_ID:", user_id)  # User IDni konsolga chiqarish (debug uchun)
    return user_id  # User ID qaytarish
