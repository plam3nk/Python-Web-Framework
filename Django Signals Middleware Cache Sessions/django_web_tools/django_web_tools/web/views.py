import random

from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.core.cache import cache

# from django.views.decorators import cache

UserModel = get_user_model()


# Create your views here.
# @cache.cache_page(5 * 60)
def index(request):
    if not cache.get('users'):
        cache.set('users', UserModel.objects.all(), 10)

    users = cache.get('users')

    context = {
        'count': random.randint(1, 100000),
        'users': users,
    }

    return render(request, 'index.html', context=context)
