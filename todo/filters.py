import django_filters

from .models import Todo


class TodoFilter(django_filters.FilterSet):
    created_at = django_filters.DateFromToRangeFilter()
    updated_at = django_filters.DateFromToRangeFilter()
    description = django_filters.CharFilter(lookup_expr='icontains')

    order_by = django_filters.OrderingFilter(
        fields=(
            ('created_at', 'created_at'),
            ('updated_at', 'updated_at'),
            ('description', 'description'),
        )
    )

    class Meta:
        model = Todo
        fields = ['title', 'description' ,'completed', 'created_at', 'updated_at', 'order_by']
