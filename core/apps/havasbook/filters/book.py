import django_filters
from core.apps.havasbook.models import BookModel
from django.db.models import Q




class BookFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Min Price')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Max Price')
    min_sold_count = django_filters.NumberFilter(field_name='sold_count', lookup_expr='gte', label='Min Sold Count')
    max_sold_count = django_filters.NumberFilter(field_name='sold_count', lookup_expr='lte', label='Max Sold Count')
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains', label='Category')
    is_discount = django_filters.BooleanFilter(field_name='is_discount', label='Discounted Books')
    search = django_filters.CharFilter(method='filter_by_search', label='Search Books')

    popular = django_filters.BooleanFilter(method='filter_by_popular', label='Popular Books')

    def filter_by_search(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) | Q(description__icontains=value)
        )


    created_at = django_filters.OrderingFilter(
        field_name='created_at',
        label='Order by Creation Date'
    )

    
    
    sold_count = django_filters.NumberFilter(field_name='sold_count', lookup_expr='exact', label='Sold Count')

    view_count = django_filters.NumberFilter(field_name='view_count', lookup_expr='exact', label='View Count')

    def filter_by_popular(self, queryset, name, value):
        if value:  
            queryset = queryset.order_by('-sold_count')  
        return queryset

    is_preorder = django_filters.BooleanFilter(field_name='is_preorder', label='Pre-order Books')

    ordering = django_filters.OrderingFilter(
        fields=(
            ('sold_count', 'sold_count'),
            ('view_count', 'view_count'),
            ('created_at', 'created_at'),
            ('price', 'price'),
            ('name', 'name'),
            ('popular', 'popular'),

        ),
        label="Order By"
    )

  

    class Meta:
        model = BookModel
        fields = [
            'min_price',
            'max_price',
            'min_sold_count',
            'max_sold_count', 
            'category',
            'is_discount',
            'is_preorder',
        ]
