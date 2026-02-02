from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages

# index view
def index(request):
    return render(request, 'index.html')

def admin_dashboard_content_views(request):
    return render(request,'accounts/admin_dashboard_content.html')

