import imp
from token import RIGHTSHIFTEQUAL
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import CustomUserCreationForm

def loginUser(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print("username does not exist")
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('learning_logs:index')
        else:
            print("username or password is incorect")


    return render(request,'users/login.html')

def logoutUser(request):
    logout(request)
    return render(request, 'users/logged_out.html')

def registerUser(request):
    if request.method != 'POST':
        form = CustomUserCreationForm()
    else:
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('learning_logs:index')

    context = {'form':form}
    return render(request,'users/register.html', context)