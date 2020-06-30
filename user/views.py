from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate


# Create your views here.
def register(request):
     
    if request.method=="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
              
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            newUser = User()
            newUser.username=username
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)
            messages.success(request,"Başaraıyla Giriş Yapıldı")
            return redirect("index")
        
        context={
            "form":form
        }
        return render(request,"register.html",context)
    else:
        form=RegisterForm()
        context={
            "form":form
        }
        return render(request,"register.html",context)

def Login(request):
    
    form= LoginForm(request.POST or None)
 
    context= {
        "form":form
    }
    if form.is_valid():

        username= form.cleaned_data.get("username")
        password= form.cleaned_data.get("password")

        user = authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"Kullanıcı Adı Veya Parola Hatalı")
            return render(request,"login.html",context)
        
        login(request,user)
        messages.success(request,"Başarıyla Giriş Yapıldı")
        return redirect("index")

    return render(request,"login.html",context)
def Logout(request):
    logout(request)
    messages.success(request,"Çıkış Yapıldı")
    return redirect("index")


