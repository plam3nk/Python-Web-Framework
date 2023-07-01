from django.urls import path

from django_cbv.web.views import list_articles, ListArticlesView, ArticleDetailView, ArticleCreateView, \
    ArticleDeleteView

urlpatterns = [
    path('', list_articles, name='list articles'),
    path('cbv/', ListArticlesView.as_view(), name='list articles cbv'),
    path('cbv/<int:pk>', ArticleDetailView.as_view(), name='details article'),
    path('cbv/create/', ArticleCreateView.as_view(), name='create article'),
    path('cbv/delete/<int:pk>', ArticleDeleteView.as_view(), name='delete article'),
]