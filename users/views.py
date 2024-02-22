from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm, UserLoginForm

def register(request):
    '''    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=raw_password)
            login(request, user)
            return redirect('index.html')

    else:
        form = RegistrationForm()
        return render(request, 'auth/register.html', {'form': form})'''



def signin(request):
   ''' if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index.html')  # Redirect to your home page or any desired page after login
    else:
        form = UserLoginForm()
    return render(request, 'auth/signin.html', {'form': form})'''




def dashboard(request):
    pass


def user_logout(request):
   ''' logout(request)
    return redirect('auth/signin.html')'''