from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login
from django.contrib.auth import forms as auth_form

# Create your views here.

# register_user, login_user, show_profile_details, edit_profile, delete_profile
UserModel = get_user_model()


class RegisterUserForm(auth_form.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')


class RegisterUserView(views.CreateView):
    form_class = RegisterUserForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        # user = self.object

        login(self.request, self.object)

        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['next'] = self.request.GET.get('next', '')

        return context

    def get_success_url(self):
        return self.request.POST.get('next', self.success_url)


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    # success_url = ''
    # def get_success_url(self):


class LogoutUserView(auth_views.LogoutView):
    pass


def register_user(request):
    return render(request, template_name='accounts/register-page.html')


def login_user(request):
    return render(request, template_name='accounts/login-page.html')


def show_profile_details(request, pk):
    return render(request, template_name='accounts/profile-details-page.html')


def edit_profile(request, pk):
    return render(request, template_name='accounts/profile-edit-page.html')


def delete_profile(request, pk):
    return render(request, template_name='accounts/profile-delete-page.html')
