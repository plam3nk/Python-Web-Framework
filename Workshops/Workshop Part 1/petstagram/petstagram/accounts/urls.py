from django.urls import path, include

from .views import show_profile_details, edit_profile, delete_profile, RegisterUserView, LoginUserView, LogoutUserView

urlpatterns = [
    # localhost:8000/accounts/register/
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/<int:pk>', include([
        path('', show_profile_details, name='profile-details'),
        path('edit/', edit_profile, name='profile-edit'),
        path('delete/', delete_profile, name='profile-delete'),
    ]))
]
