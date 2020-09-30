from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.exchange_list, name='exchanges_list'),
    path('detail/<str:code>/', views.exchange_detail, name='exchanges_detail'),
    path('create/', views.exchange_create, name='exchanges_create'),
    path('update/<str:code>/', views.exchange_update, name='exchanges_update'),
]