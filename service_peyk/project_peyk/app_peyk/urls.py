from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe_coin, name='subscribe_coin'),
    path('price/', views.get_price_history, name='get_price_history'),
]
