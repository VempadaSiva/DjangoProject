
from django.shortcuts import render,redirect
from .models import Hero,Age
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate,logout as auth_logout
from django.contrib import messages


def index(request):
    agee = Age.objects.all()
    return render(request, 'index.html',{'ag':agee})
def profiles(request):
    data = Hero.objects.all()
    gender=request.POST.get('gender')
    age=request.POST.get('age')
    state=request.POST.get('state')
    city=request.POST.get('city')
    if gender :
        data=data.filter(gender=gender)
    if age :
        data=data.filter(age=age)
    if state :
        data=data.filter(state=state)
    if city :
        data=data.filter(city=city)
    return render(request, 'profiles.html',{'data':data})
def step(request):
    agee=Age.objects.all()
    return render(request, 'step1.html',{'ag':agee})
def store(request):
    uid=request.POST.get('id')
    firstname = request.POST.get('firstname')
    secondname = request.POST.get('secondname')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    gender = request.POST.get('gender')
    agl = request.POST.get('age')
    hobbies = request.POST.get('hobbies')
    state = request.POST.get('state')
    city = request.POST.get('city')
    photo = request.FILES.get('photo')
    text=request.POST.get('text')
    agi=Age.objects.get(id=agl)
    if uid =='':
        s=Hero(firstname=firstname,secondname=secondname,email=email,phone=phone,gender=gender,age=agi,hobbies=hobbies,
           state=state,city=city,photo=photo,text=text)
        s.save()
        return render(request, 'step1.html')
    else:
        s=Hero.objects.filter(id=uid).update(firstname=firstname,secondname=secondname,email=email,phone=phone,gender=gender,age=agi,hobbies=hobbies,
           state=state,city=city,photo=photo,text=text)
        return render(request,'step1.html', {'s':s})


def viewprofile(request,id):
    sad=Hero.objects.get(id=id)
    return render(request, 'viewprofile.html',{'sad':sad})
def edit(request,id):
    don=Hero.objects.get(id=id)
    agee = Age.objects.all()
    return render(request,'step1.html', {'s':don ,'ag':agee})


def delete(request,id):
    srinu=Hero.objects.get(id=id)
    srinu.delete()
    return redirect('index')

def register(request):
    if request.method == 'POST':
        first=request.POST.get('first')
        second=request.POST.get('second')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        if password==confirmpassword:
             if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return  redirect(index)
             else:
                user=User.objects.create_user(username=email,first_name=first,last_name=second,email=email,password=password)
                Log_User=authenticate(username=email, password='password')
                auth.login(request,user)
                messages.success(request, 'Form submitted succesfully....')
                return redirect(index)
        else:
            messages.error(request, 'username or password are not matching')
            return redirect(index)
    else:
        return render(request, 'index.html')
def login(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        raw_password=request.POST.get('password')
        user=auth.authenticate(username=uname, password=raw_password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logined...........')
            return redirect(index)
        else:
            messages.error(request, 'Invalid credentials......')
            return redirect(index)
    else:
        return redirect(login)
def logout(request):
    auth_logout(request)
    return redirect(index)











