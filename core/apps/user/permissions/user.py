from rest_framework import permissions
from core.apps.shared.utils.jwt import get_claim  # get_claim funksiyasini import qilish
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from django.utils.translation import gettext_lazy as _


class UserPermission(permissions.BasePermission):
    message = _("Permission denied")

    def __call__(self, *args, **kwargs):
        return self

    def has_permission(self, request: Request, view):
        token = request.headers.get("token", None)
        print("TOKEN:", token)  

        if token is None:
            return False 
        claim = get_claim(token)

        if claim is None:
            return False 

        user_id = claim.get("user_id", None)
        print("USER_ID:", user_id)
        if user_id is None:
            return False 
        request.user_id = user_id

        return True 
