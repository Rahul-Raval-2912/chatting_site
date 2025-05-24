from django.shortcuts import render

def login_view(request):
    return render(request, 'chat/login.html')

def register_view(request):
    return render(request, 'chat/register.html')
