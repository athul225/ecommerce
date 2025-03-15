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
            data=Users.objects.create(name=name,email=email,uname=uname,pwd=pwd)
            data.save()
            return redirect(login)
        else:
            print("password doesn't match")
            return redirect(register)
    
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        uname=request.POST['Uname']
        pwd=request.POST['pwd']
        
        try:
            data=Users.objects.get(pwd=pwd,uname=uname)
            request.session['user']=uname
            return redirect(firstpage)
            
        except:
            print('Not found')
            return redirect(login)
    
    return render(request,'login.html')

def firstpage(request):
    
    return render(request,'firstpage.html')


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect(login)
    else:
        return redirect(login)
    

def adminlogin(request):
    if request.method=='POST':
        uname=request.POST['Uname']
        pwd=request.POST['pwd']
        
        try:
            data=admin.objects.get(pwd=pwd,uname=uname)
            request.session['admin']=uname
            return redirect(index)
            
        except:
            print('Not found')
            return redirect(adminlogin)
    
    return render(request,'adminlogin.html')
    

def adminregister(request):
    if request.method=='POST':
        name=request.POST['Name']
        email=request.POST['Email']
        uname=request.POST['Uname']
        pwd=request.POST['Password']
        cnf_pwd=request.POST['cnf_pwd']
        if cnf_pwd==pwd:
            data=admin.objects.create(name=name,email=email,uname=uname,pwd=pwd)
            data.save()
            return redirect(adminlogin)
        else:
            print("password doesn't match")
            return redirect(adminregister)

    return render(request,'adminregister.html')

def index(request):

    return render(request,'index.html')


def product(request):
    products = Product.objects.all()

    return render(request, 'index.html', {'products': products})