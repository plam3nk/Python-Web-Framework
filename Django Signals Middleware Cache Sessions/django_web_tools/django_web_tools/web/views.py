import random

from django.shortcuts import render
from django.views.decorators import cache


# Create your views here.
@cache.cache_page(5)
def index(request):
    context = {
        'count': random.randint(1, 100000)
    }
    return render(request, 'index.html', context=context)
