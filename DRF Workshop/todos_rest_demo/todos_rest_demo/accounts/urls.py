from django.urls import path

from todos_rest_demo.accounts.views import ApiRegisterView, ApiLoginView, ApiLogoutView

urlpatterns = (
    path('register/', ApiRegisterView.as_view(), name='api_register_view'),
    path('login/', ApiLoginView.as_view(), name='api_register_view'),
    path('logout/', ApiLogoutView.as_view(), name='api_register_view'),
)