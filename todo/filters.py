import django_filters

from .models import Todo


class TodoFilter(django_filters.FilterSet):

    # create_atで、範囲指定し検索
    created_at = django_filters.DateFromToRangeFilter()
    title = django_filters.CharFilter(lookup_expr='icontains')

    # descriptionを含むかどうかで検索
    description = django_filters.CharFilter(lookup_expr='icontains')

    order_by = django_filters.OrderingFilter(
        fields=(
            ('created_at', 'created_at'),
            ('updated_at', 'updated_at'),
            ('title', 'title'),
            ('id', 'id'),
        )
    )

    class Meta:
        model = Todo
        fields = ['title', 'completed', 'created_at', 'updated_at', 'order_by',]
