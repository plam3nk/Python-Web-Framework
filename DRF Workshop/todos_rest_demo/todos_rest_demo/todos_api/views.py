from django.shortcuts import render
from rest_framework import generics as api_views, serializers

from todos_rest_demo.todos_api.models import Todo, Category
from todos_rest_demo.todos_api.serializers import CategorySerializer, TodosSerializer


# Create your views here.
class TodosCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

    def to_internal_value(self, data):
        instance = super().to_internal_value(data)
        instance['user'] = self.context['request'].user

        return instance


class CategoriesApiListView(api_views.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TodosApiView(api_views.ListCreateAPIView):
    queryset = Todo.objects.all()
    list_serializer_class = TodosSerializer
    create_serializer_class = TodosCreateSerializer

    def get_serializer_class(self):
        if self.__is_get(self.request):
            return self.list_serializer_class

        return self.create_serializer_class

    def get_queryset(self):
        queryset = super().get_queryset()

        if not self.__is_get(self.request):
            return queryset

        queryset = queryset.filter(user=self.request.user)

        category_id = self.request.query_params.get('category', None)

        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset

    @staticmethod
    def __is_get(request):
        return request.method == 'GET'
