from django_filters import rest_framework as filters

from ..models import PreorderModel


class PreorderFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = PreorderModel
        fields = ("name",)
