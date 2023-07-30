from rest_framework import serializers

from todos_rest_demo.todos_api.models import Todo, Category


class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'