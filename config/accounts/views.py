from django.views.generic import TemplateView


class AccountView(TemplateView):
    template_name = "accounts/account.html"


class LoginView(TemplateView):
    template_name = "accounts/login.html"



class RegisterView(TemplateView):
    template_name = "accounts/register.html"
