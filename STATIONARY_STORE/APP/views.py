from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .models import Product

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

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('index')
    return redirect('product_items')

def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.des = request.POST.get('des')
        product.price = request.POST.get('price')
        product.offerprice = request.POST.get('offerprice')
        
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        
        product.save()
        return redirect('product_items')

    return render(request, 'update_product.html', {'product': product})



def allproduct(request):
    products=Product.objects.all()
    
    return render(request,'allproduct.html',{'products':products})
    