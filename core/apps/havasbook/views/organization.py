from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny


class OrganizationView(ReadOnlyModelViewSet):
    # queryset = Model.objects.all()
    # serializer_class = Serializer
    permission_classes = [AllowAny]
