from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate, get_user_model
#from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import LoginForm, UserRegistrationForm

# Create your views here.
#User = get_user_model()


# class CustomLoginView(LoginView):
#     template_name = "accouts/login.html"
#     fields = "__all__"
#     #redirect_authenticated_user = True
#     success_url = reverse_lazy('')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Uwierzytelnienie zakończyło się sukcesem.')
                else:
                    return HttpResponse('Konto jest zablokowane. Zgłoś się do administratora')
            else:
                return HttpResponse('Nieprawidłowe dane uwierzytelniające.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid:
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'accounts/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        return render(request, 'accounts/register.html',{'user_form': user_form})

# class CustomLogoutView(LoginView):
#     template_name = "accounts/templates/registration/logged_out.html"
#     fields = "__all__"
#     #redirect_authenticated_user = True
#     success_url = reverse_lazy('index')
#
# class RegisterView(FormView):
#     template_name = "accouts/templates/accounts/register.html"
#     form_class = CustomUserCreationForm
#     # redirect_authenticated_user = True
#     # success_url = reverse_lazy("index")
#
# class MainView(FormView):
#     template_name = "accouts/../viewer/templates/main.html"
#     form_class = CustomUserCreationForm
#     # redirect_authenticated_user = True
#     # success_url = reverse_lazy("index")
#
#     def form_valid(self, form):
#         user = form.save()
#         if user is not None:
#             login(self.request, user)
#         return super(RegisterView, self).form_valid(form)



