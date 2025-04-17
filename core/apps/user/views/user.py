from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from ..models import UserModel
from ..serializers.user import CreateUserSerializer, ListUserSerializer, RetrieveUserSerializer
from ..permissions import UserPermission  # siz yozgan permission



@extend_schema(tags=["user"])
class UserView(BaseViewSetMixin, ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = ListUserSerializer
    permission_classes = [AllowAny]  
    action_permission_classes = {
        "create": [UserPermission],
    }
    action_serializer_class = {
        "list": ListUserSerializer,
        "retrieve": RetrieveUserSerializer,
        "create": CreateUserSerializer,
    }

    def create(self, request, *args, **kwargs):
        bot_user_pk = request.bot_user 

        if isinstance(bot_user_pk, UserModel):
            return Response({"detail": "Foydalanuvchi allaqachon mavjud."}, status=status.HTTP_400_BAD_REQUEST)

        data = request.data.copy()
        data["id"] = bot_user_pk  

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
