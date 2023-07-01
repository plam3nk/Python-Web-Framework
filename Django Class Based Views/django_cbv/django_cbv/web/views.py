from django import forms
from django.forms import modelform_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from django_cbv.web.models import Article


# Create your views here.

# View in Django.
# 1. View must be callable
# 2. Returns HttpResponse object.

def list_articles(request):
    context = {
        'articles': Article.objects.all(),
    }

    return render(request,
                  'articles/list.html',
                  context)


# views.CreateView
# views.ListView
# views.UpdateView
# views.DeleteView
# views.DetailView

# class BaseView():
#
#     def get(self, request):
#         pass
#
#     def post(self, request):
#         pass
#
#     @classmethod
#     def as_view(cls):
#         self = cls()
#
#         def view(request):
#             if request.method == 'GET':
#                 return self.get(request)
#
#             else:
#                 return self.post(request)
#
#         return view


# class ListArticlesView(views.View):
#
#     def get(self, request):
#         context = {
#             'articles': Article.objects.all(),
#         }
#
#         return render(self.request,
#                       'articles/list.html',
#                       context)

# class ListArticlesView(views.TemplateView):
#     template_name = 'articles/list.html'
#
#     # static_data
#     extra_context = {
#         'articles': Article.objects.all()
#     }
#
#     # dynamic data
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['articles'] = Article.objects.all()
#         return context


class ListArticlesView(views.ListView):
    template_name = 'articles/list.html'
    model = Article
    # context_object_name = 'articles' # Default is 'object_list'

    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        search = self.request.GET.get('search', '')
        queryset = queryset.filter(title__icontains=search)

        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['search'] = self.request.GET.get('search', '')

        return context


# /pk
# /slug
# /pk/slug , /slug/pk
# ↓ ↓ ↓

class ArticleDetailView(views.DetailView):
    model = Article
    template_name = 'articles/detail.html'
    # pk_url_kwarg = 'id'


class RedirectToArticlesView(views.RedirectView):
    url = reverse_lazy('list_articles_cbv')


# reverse() vs reverse_lazy()
class DisabledFormFieldsMixin:
    disabled_fields = ()

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)

        for field in self.disabled_fields:
            form.fields[field].widget.attrs['disabled'] = 'disabled'
            form.fields[field].widget.attrs['readonly'] = 'readonly'

        return form


class ArticleCreateView(DisabledFormFieldsMixin, views.CreateView):
    model = Article
    template_name = 'articles/create.html'

    fields = '__all__'

    success_url = reverse_lazy('list articles cbv')

    disabled_fields = ('title',)

    # form_class = modelform_factory(
    #     Article,
    #     fields=('title', 'content'),
    #     widgets={
    #         'tittle': forms.TextInput(
    #             attrs={
    #                 'class': 'abc'
    #             }
    #         )
    #     }
    # )


class ArticleUpdateView(views.UpdateView):
    pass


class ArticleDeleteView(DisabledFormFieldsMixin, views.DeleteView):
    model = Article
    template_name = 'articles/delete.html'

    disabled_fields = ('title', 'content',)

    form_class = modelform_factory(
        Article,
        fields=('title', 'content'),
    )

    success_url = reverse_lazy('list articles cbv')

    def get_form_kwargs(self):
        instance = self.get_object()
        form_kwargs = super().get_form_kwargs()

        form_kwargs.update(instance=instance)

        return form_kwargs
