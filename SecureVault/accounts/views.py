from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login


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
            return redirect("upload_key")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {"form": form})


def profile_view(request):
    return render(request, 'profile.html')
