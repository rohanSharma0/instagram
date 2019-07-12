from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth , User
from .forms import UserRegisterForm ,UserUpdateForm , ProfileUpdateForm ,ProfileImageForm


# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect ('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            pwd = request.POST['password']

            user = auth.authenticate(username= username, password=pwd)
            if user is not None:
                auth.login(request,user)
                return redirect('home')
            else:
                # messages.error(request,'Invalid credentials')
                return redirect('login')
        else:
            return render(request,'users/login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect ('home')
    else:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = UserRegisterForm()

        template_name = 'users/register.html'
        context={
            'form':form
        }
        return render(request , template_name , context)

@login_required
def editprofile(request,username):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST ,instance=request.user)
        p_form = ProfileUpdateForm(request.POST ,instance=request.user.profile)
        profileimg_form = ProfileImageForm(request.POST ,instance=request.user.profile)

        if profileimg_form.is_valid():
            profileimg_form.save()
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
        return redirect('home')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        profileimg_form = ProfileImageForm(instance=request.user.profile)
    
    template_name = 'main/editprofile.html'
    context = {
        'u_form' : u_form,
        'p_form' : p_form,
        'profileimg_form' :profileimg_form
    }
    return render(request , template_name , context)

@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')
