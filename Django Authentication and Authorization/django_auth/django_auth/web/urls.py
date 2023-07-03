from django.views import generic as views
from django.urls import path

from django_auth.web.views import index, user_login, logout_user

urlpatterns = (
    path('', index, name='index'),
    path('login/', user_login, name='login'),
    path('logout/', logout_user, name='logout'),
)