import django_filters

from .models import Todo


class TodoFilter(django_filters.FilterSet):
    created_at = django_filters.DateFromToRangeFilter()
    updated_at = django_filters.DateFromToRangeFilter()
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Todo
        fields = ['title', 'description' ,'completed', 'created_at', 'updated_at']
