from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, login, logout, authenticate, update_session_auth_hash
from django.contrib import messages
from .forms import UserRegistrationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required

...


def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"New account Created: {user.username}")
            return redirect('/')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name="register.html",
        context={"form": form}
    )


def custom_login(request):
    if request.user.is_authenticated:
        return redirect('posts')

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )

            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect('login')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
                return redirect('login')

    form = AuthenticationForm()

    return render(
        request=request,
        template_name="login.html",
        context={'form': form}
    )


@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("posts")


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'edit_password.html', {
        'form': form
    })
