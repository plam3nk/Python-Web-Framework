from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import forms as auth_forms, login, authenticate, get_user_model
from django.contrib.auth import views as auth_views
from django.contrib.auth import mixins as auth_mixins
from django.utils.translation import gettext_lazy as _

from django_upm.web.models import Profile

# Create your views here.
UserModel = get_user_model()


# app_auth/views.py

class RegisterUserForm(auth_forms.UserCreationForm):
    content = forms.BooleanField()
    first_name = forms.CharField(
        max_length=30,
        required=True
    )

    password2 = forms.CharField(
        label=_("Repeat password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Repeat password, please"),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].help_text = _('It works')

    def save(self, commit=True):
        user = super().save(commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            user=user
        )
        if commit:
            profile.save()

        return user

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


# def register_view(request):
#     if request.method == 'GET':
#         form = RegisterUserForm()
#
#     else:
#         form = RegisterUserForm(request.POST)
#
#         if form.is_valid():
#             # form_valid(form)
#             form.save()
#             # redirect
#
#         # redirect
#     # ....

class RegisterUserView(views.CreateView):
    template_name = 'app_auth/register.html'
    form_class = RegisterUserForm
    # Static way of providing 'success_url'
    success_url = reverse_lazy('register user')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result
    # ============================================
    # Dynamic way of providing 'success_url'
    # def get_success_url(self):
    #     pass
    # ============================================
    # def get_form_class(self):
    #     if condition1:
    #         return Condition1Form
    #     elif condition2:
    #         return Condition2Form
    #     else:
    #         return Condition3Form
    # ============================================


class LoginUserView(auth_views.LoginView):
    template_name = 'app_auth/login.html'
    extra_context = {'title': 'Login', 'link_title': 'Register'}


class LogoutUserView(auth_views.LogoutView):
    pass


# @login_required
# def func_view(request):
#     pass


class UsersListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    template_name = 'app_auth/users_list.html'
    # Login URL only for this view.
    # login_url = 'custom-login/url'
