# authentication/views.py
from django.shortcuts import render

def login_view(request):
    return render(request, 'Login.html')