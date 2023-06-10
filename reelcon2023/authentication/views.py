from django.shortcuts import render,redirect
from .forms import SignupForm
from django.contrib.auth import login
# Create your views here.
def signup(response):
    if response.method == "POST":
        form = SignupForm(response.POST)
        if form.is_valid():
            user=form.save()
            instagram_username = form.cleaned_data['instagram_username']
            instagram_profile_link = form.cleaned_data['instagram_profile_link']
            phone_number = form.cleaned_data['phone_number']
            user.save()
            login(response,user)
            return redirect("/")
    else:
        form = SignupForm()
    return render(response,"authentication/signup.html",{"form":form})