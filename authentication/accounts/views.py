# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        # Retrieve email and password from the form
        em = request.POST.get("email")
        pwd = request.POST.get("password")
        
        # Authenticate the user
        user = authenticate(request, username=em, password=pwd)
        
        if user is not None:
            # Log the user in and redirect to the dashboard
            login(request, user)
            return redirect("/dashboard")
        else:
            # If authentication failed, show an error message
            messages.error(request, "Invalid email or password.")
    
    # Render the login page
    return render(request, 'Login.html')
