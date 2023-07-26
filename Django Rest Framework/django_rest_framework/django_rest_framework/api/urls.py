from django.urls import path

from django_rest_framework.api.views import AuthorsApiView

urlpatterns = (
    path('authors/', AuthorsApiView.as_view(), name='api_list_authors')
)