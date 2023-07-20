from django.urls import path

from django_deploy.accounts.views import LoginUserView, RegisterUserView

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('register/', RegisterUserView.as_view(), name='register_user'),
)