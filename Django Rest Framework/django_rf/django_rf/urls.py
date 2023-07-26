"""
URL configuration for django_rf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django_rf.web.urls')),
    path('accounts/', include('django_rf.accounts.urls')),
    path('api/', include('django_rf.api.urls'))
]

'''
REST -> Representational State Transfer
API -> Application Programming Interface

(JSON, XML, YAML)

=> REST API

Author (first_name, last_name)
Book (title, description, author)

# Authors: /authors/

C -> Create author
POST /authors/

R -> Get all authors
GET /authors/

R -> Get author details
GET /authors/{ID}/

{
    'first_name': 'Doncho',
    'last_name': 'Minkov'
}

U -> Update author
PUT /authors/{ID}/
{
    'first_name': 'Doncho 2',
    'last_name': 'Minkov'
}

PATCH /authors/{ID}/
{
    'first_name': 'Doncho 2'
}

D -> Delete author
DELETE /authors/{ID}/

## Actions

POST /authors/{ID}/upvote/

# Summarize:

GET /authors/
POST /authors/

GET /authors/{ID}/
PUT /authors/{ID}/
(PATCH /authors/{ID}/)
DELETE /authors/{ID}/
'''

'''
type2 is a text format (JSON, txt, csv, XML)

Serialization -> obj(type1) -> obj2(type2)
Deserialization -> obj2(type2) -> obj(type1) 

'''

'''
AJAX - Asynchronous JavaScript and XML
'''
