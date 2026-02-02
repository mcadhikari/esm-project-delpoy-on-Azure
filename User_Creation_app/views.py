from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")       # input name="email"
        password = request.POST.get("password") # input name="password"

        # authenticate
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)   # log user in
            return redirect("admin-dashboard-content")   # redirect to dashboard for now
        else:
            messages.error(request, "Invalid email or password, try again.")

    return render(request, "userlogin.html")
