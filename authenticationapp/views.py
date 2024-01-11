from django.shortcuts import render , redirect
from .models import Profile
from .forms import ProfileForm 
from django.contrib.auth.models import User 
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout 

# Create your views here.

def SignUp(request):
    if request.method == "POST":
        form = ProfileForm(request.POST , request.FILES)
        if form.is_valid():
            try:
                fullname = form.cleaned_data['fullname']
                email = form.cleaned_data['email']
                contactno = form.cleaned_data['contactno']
                address = form.cleaned_data['address']
                documents = form.cleaned_data['documents']
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                confirm_password = form.cleaned_data['confirm_password']
                

                if password != confirm_password:
                    form.add_error('confirm_password',"Password and Confirm password are dismatch")
                    return render(request,'signup.html',{'form':form})
                
                hashed_password = make_password(password)
                user = User.objects.create(username=username,password=hashed_password,email=email)
                prof = Profile.objects.create(user=user,fullname=fullname,contactno=contactno,address=address,documents=documents)
                return redirect('LoginView')
            except Exception as e:
                print(e)
    form = ProfileForm()
    return render(request,'signup.html',{'form':form})


def LoginView(request):
    if 'username' in request.session:
        user_profile = request.user
        return redirect('userapp:Home')

    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                request.session['authenticated'] = True
                request.session['username'] = username
                user_profile = Profile.objects.get(user=user)
                login(request,user)
                return redirect('userapp:Home')

    form = AuthenticationForm()
    return render(request,'login.html',{'form':form})


def LogoutView(request):
    if request.session.get('authenticated'):
        request.session.flush()
    return redirect('LoginView')

    
