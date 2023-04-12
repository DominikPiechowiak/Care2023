from django.http import HttpResponse
from django.contrib.auth import login, get_user_model
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
# from django.urls import reverse_lazy
from django.views.generic import FormView


# Create your views here.
User = get_user_model()


class CustomLoginView(LoginView):
    template_name = "login.html"
    fields = "__all__"
    # redirect_authenticated_user = True


class RegisterView(FormView):
    template_name = "register.html"
    form_class = CustomUserCreationForm
    # redirect_authenticated_user = True
    # success_url = reverse_lazy("index")

class MainView(FormView):
    template_name = "main.html"
    form_class = CustomUserCreationForm
    # redirect_authenticated_user = True
    # success_url = reverse_lazy("index")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)



