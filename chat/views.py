from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from raven_project.chat.forms import RegisterForm

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")  # Create this URL later
        else:
            return HttpResponse("Invalid username or password.")
    return render(request, "chat/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # You can create login page later
    else:
        form = RegisterForm()
    return render(request, 'chat/register.html', {'form': form})