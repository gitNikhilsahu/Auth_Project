from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm

from .forms import SignUpForm

def Home_Page(request):
    template = 'WebApp/Home.html'
    return render(request, template)

@login_required()
def Customer(request):
    template = 'WebApp/Customer.html'
    return render(request, template)

def Logout_View(request):
    template = 'WebApp/Logout.html'
    return render(request, template)

def Signup_View(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    template = 'Registration.html'
    context = {'form': form}
    return render(request, template, context)
