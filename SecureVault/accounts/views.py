from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("upload_key")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("upload_key")  # Changed to redirect to profile
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {"form": form})


@login_required(login_url='login')
def profile_view(request):
    # Pass user data to template
    context = {
        'user': request.user,
        'user_id': request.user.id,
    }
    return render(request, 'profile.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')
