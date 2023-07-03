import random

from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from django_auth.settings import LOGIN_URL

# Create your views here.
UserModel = get_user_model()


@login_required
def index(request):
    suffix = random.randint(1, 10000)
    # Don't use 'objects.create(...)'
    # instead use this or DjangoAdmin:
    user = UserModel.objects.create_user(
        username=f'plamen_{suffix}',
        password='123456789',
    )
    specific_user = UserModel.objects.get(username='plamen_8609')
    # print(request.user)
    # login(request, user)
    # user = UserModel.objects.get(username='plamen')
    context = {
        'user': request.user,
        'permission': request.user.has_perm('auth.view_user'),
        'specific_user': specific_user.has_perm('auth.view_user'),
    }
    return render(request, 'index.html', context)


def user_login(request):
    # Authentication
    user = authenticate(
        username=f'plamen_8609',
        password='123456789',
    )

    print(f'User: {user}')
    # Authorization
    login(request, user)
    return redirect('index')


def logout_user(request):
    logout(request)

    return redirect('index')


class IndexView(views.TemplateView, LoginRequiredMixin):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        pass
