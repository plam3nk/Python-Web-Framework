import random

from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.core.cache import cache

from django_web_tools.web.models import Task

# from django.views.decorators import cache

UserModel = get_user_model()


# Create your views here.
# @cache.cache_page(5 * 60)
def index(request):
    request.session['count'] = request.session.get('count', 0) + 1

    if not cache.get('users'):
        cache.set('users', UserModel.objects.all(), 10)

    users = cache.get('users')

    prev_tasks_ids = request.session.get('prev_tasks', [])

    context = {
        # 'count': random.randint(1, 100000),
        'count': request.session['count'],
        'users': users,
        'tasks': Task.objects.all(),
        'prev_tasks': Task.objects.filter(pk__in=prev_tasks_ids),
    }

    return render(request, 'index.html', context=context)


def create_task(request):
    Task.objects.create(title=f'Task {random.randint(1, 100000)}')

    return redirect('index')


def details_task(request, pk):
    task = Task.objects.filter(pk=pk) \
        .get()

    prev_tasks = request.session.get('prev_tasks', [])

    prev_tasks.append(task.pk)
    start_index = max(
        0,
        len(prev_tasks) - 3,
    )
    request.session['prev_tasks'] = prev_tasks[start_index:]
    print(request.session['prev_tasks'])
    return redirect('index')
