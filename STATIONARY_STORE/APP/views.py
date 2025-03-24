from django.shortcuts import render,redirect,get_object_or_404
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




def logout(request):
    if request.user.is_authenticated:
        Users.logout(request)
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
    products=Product.objects.all()
    if request.method=='POST':
        image=request.FILES['image']
        name=request.POST['name']
        des=request.POST['des']
        price=request.POST['price']
        offerprice=request.POST['offerprice']
        
        data=Product.objects.create(image=image,name=name,des=des,price=price,offerprice=offerprice)
        data.save()
        return redirect(index)

    return render(request,'index.html',{'docs':products})


def product(request):
    products = Product.objects.all()

    return render(request, 'index.html', {'products': products})
def firstpage(request):
    products = Product.objects.all()
    return render(request,'firstpage.html',{'products':products})

def product_items(request):
    products = Product.objects.all()

    return render(request, 'product_items.html',{'products':products})
def delete_product(request,pk): 
    Product.objects.filter(pk=pk).delete()
    return redirect(index)