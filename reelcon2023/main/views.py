from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
@login_required
def home(response):
        return render(response,"main/home.html")