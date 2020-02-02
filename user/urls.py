from django.urls import path, include
from django.conf import settings
from .views import login_views, register_views,LogoutView,profileView
urlpatterns = [
    path('register/', register_views.as_view(), name='register'),
    path('login/', login_views.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profileView.as_view(), name='profile'),
]
