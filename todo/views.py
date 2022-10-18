from rest_framework import viewsets

from .filters import TodoFilter
from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filterset_class = TodoFilter
    
