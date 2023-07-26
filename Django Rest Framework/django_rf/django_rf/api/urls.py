from django.urls import path
from rest_framework.routers import DefaultRouter

from django_rf.api.views import AuthorsApiView, AuthorsView, AuthorsApiViewSet

router = DefaultRouter()

router.register('authors-vs', AuthorsApiViewSet, basename='author')

print(router.urls)

urlpatterns = [
    *router.urls,
    path('authors/', AuthorsApiView.as_view(), name='api_list_authors'),
    path('authors-ssr/', AuthorsView.as_view(), name='list_authors'),
    path('authors-vs/', AuthorsApiViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }))
]