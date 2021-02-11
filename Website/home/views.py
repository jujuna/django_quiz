from django.shortcuts import render, HttpResponse
from .forms import SignUpForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect


from django.contrib.auth.forms import authenticate
from django.contrib.auth import login
from django.urls import reverse



def home(request):
    if request.method=="POST":
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse("question:home"))
            
    else:  
        form = SignUpForm()
        
        
    return render(request, 'home/home.html', {'form': form})

def about(request):
    return render (request, 'home/about.html')