from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from Login.forms import SignUpForm,userProfilechange,ProfilePic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.


def sign_up(request):
    form=SignUpForm()
    registered=False
    if request.method =='POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered=True

    dict={'form':form,'registered':registered}
    return render (request,'Login/sign_up.html',context=dict)


def login_page(request):
    form=AuthenticationForm()
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
    return render (request,'Login/login.html',context={'form':form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def profile(request):
    return render (request,'Login/profile.html',context={})

@login_required
def user_change(request):
    current_user=request.user
    form=userProfilechange(instance=current_user)
    if request.method=='POST':
        form=userProfilechange(request.POST,instance=current_user)
        if form.is_valid():
            form.save()
            form=userProfilechange(instance=current_user)
    return render(request,'Login/chnage_profile.html',context={'form':form})


@login_required
def add_pro_pic(request):
    form = ProfilePic()
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('Login:profile'))
    return render(request, 'Login/pic_add.html', context={'form':form})
