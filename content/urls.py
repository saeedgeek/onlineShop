from .views import *
from django.urls import path,include
urlpatterns = [
    path('cart/', Cart.as_view(),name='cart'),

]
