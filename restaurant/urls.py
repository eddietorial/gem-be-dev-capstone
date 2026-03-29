from django.urls import path
from . import views

urlpatterns = [
    # Static pages
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('book/', views.book, name='book'),

    # Menu REST API
    path('menu/items/', views.MenuItemView.as_view(), name='menu-list'),
    path('menu/items/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),
]
