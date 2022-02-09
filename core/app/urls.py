from django.urls import path
from .views import CategoryListView, ProductsListView

urlpatterns = [
    path('categories/', 
            CategoryListView.as_view()),
    path('category-products/<int:pk>/', 
            ProductsListView.as_view(),
            name='category-detail'),
]