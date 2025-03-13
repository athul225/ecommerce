from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def register(request):
    if request.method=='POST':
        name=request.POST['Name']
        email=request.POST['Email']
        uname=request.POST['Uname']
        pwd=request.POST['Password']
        cnf_pwd=request.POST['cnf_pwd']
        if cnf_pwd==pwd:
            data=User.objects.create(name=name,email=email,uname=uname,pwd=pwd)
            data.save()
        else:
            print("password doesn't match")
    
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        uname=request.POST['Email']
        pwd=request.POST['pwd']
        
        try:
            data=User.objects.get(pwd=pwd,uname=uname)
            request.session['user']=uname
            return redirect(index)
            
        except:
            print('Not found')
            return redirect(login)
    
    return render(request,'login.html')

def index(request):
    
    return render(request,'index.html')