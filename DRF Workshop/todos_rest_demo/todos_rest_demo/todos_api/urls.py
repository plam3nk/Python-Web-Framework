from django.urls import path

from todos_rest_demo.todos_api.views import TodosApiView, CategoriesApiListView

urlpatterns = (
    path('', TodosApiView.as_view(), name='api todos'),
    path('categories/', CategoriesApiListView.as_view(), name='api_todo_categories')
)