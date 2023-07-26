from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views import generic as views
from rest_framework import generics as api_views, serializers

from django_rest_framework.api.models import Author


# @api_view
# def rest_view(request):
#     pass


# Server-side rendering (Templates)
# class AuthorsView(views.ListView):
#     queryset = Author.objects.all()
#
#     template_name = '...'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorsApiView(api_views.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
