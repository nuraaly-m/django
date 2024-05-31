
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from . import models, middlewares, forms


class RegistrationView(CreateView):
    form_class = forms.CustomRegistrationForm
    template_name = "users/registration.html"
    success_url = "/login/"

    def form_valid(self, form):
        response = super().form_valid(form)
        exp = form.cleaned_data["experience"]
        if exp < 1:
            self.object.club = "Новичок"
        elif 1 <= exp <= 2:
            self.object.club = "Средний"
        elif 2 <= exp <= 3:
            self.object.club = "Мастер"
        elif 3 <= exp <= 5:
            self.object.club = "Профи"
        else:
            self.object.club = "Без опыта"

        self.object.save()
        return response


class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "users/login.html"
    success_url = '/books'

class AuthLogoutView(LogoutView):
    next_page = reverse_lazy("users:login")
