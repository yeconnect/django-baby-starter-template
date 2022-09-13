from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("list/", views.BlogListView.as_view()),
    path("detail/<int:pk>/", views.BlogDetailView.as_view()),
]
