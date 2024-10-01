from django.shortcuts import render
from . import models
from django.urls import reverse
from django.shortcuts import render, redirect
import datetime
from django.views.decorators.csrf import csrf_protect
# Create your views here.

def products(request):
      return render(request,'website_app/products.html')
      
@csrf_protect
def order_1(request):
    current_time = datetime.datetime.now()
    if request.method=='POST':
        name=request.POST["first_name"]
        surname=request.POST["last_name"]
        telephone=request.POST["telephone"]
        province=request.POST["province"]
        district=request.POST["district"]
        address=request.POST["address"]
        number = request.POST["number"]
        size=request.POST["size"]
        colour=request.POST["colour"]
        payment_method=request.POST["payment_method"]
        product_id = 1
        models.Customer.objects.create(product_id=product_id, name=name,surname=surname,telephone=telephone,province=province,district=district,
                                       address=address,number=number,size=size,colour=colour,payment_method=payment_method,date=current_time)
        

        return redirect(reverse('website_app:order_success'))
    else:
        return render(request,'website_app/order_1.html')

@csrf_protect
def order_2(request):
    current_time = datetime.datetime.now()
    if request.method=='POST':
        name=request.POST["first_name"]
        surname=request.POST["last_name"]
        telephone=request.POST["telephone"]
        province=request.POST["province"]
        district=request.POST["district"]
        address=request.POST["address"]
        number = request.POST["number"]
        size=request.POST["size"]
        colour=request.POST["colour"]
        payment_method=request.POST["payment_method"]
        product_id = 2
        models.Customer.objects.create(product_id=product_id, name=name,surname=surname,telephone=telephone,province=province,district=district,
                                       address=address,number=number,size=size,colour=colour,payment_method=payment_method,date=current_time)
        

        return redirect(reverse('website_app:order_success'))
    else:
        return render(request,'website_app/order_2.html')

@csrf_protect
def order_3(request):
    current_time = datetime.datetime.now()
    if request.method=='POST':
        name=request.POST["first_name"]
        surname=request.POST["last_name"]
        telephone=request.POST["telephone"]
        province=request.POST["province"]
        district=request.POST["district"]
        address=request.POST["address"]
        number = request.POST["number"]
        size=request.POST["size"]
        colour=request.POST["colour"]
        payment_method=request.POST["payment_method"]
        product_id = 3
        models.Customer.objects.create(product_id=product_id, name=name,surname=surname,telephone=telephone,province=province,district=district,
                                       address=address,number=number,size=size,colour=colour,payment_method=payment_method,date=current_time)
        

        return redirect(reverse('website_app:order_success'))
    else:
        return render(request,'website_app/order_3.html')


@csrf_protect
def order_4(request):
    current_time = datetime.datetime.now()
    if request.method=='POST':
        name=request.POST["first_name"]
        surname=request.POST["last_name"]
        telephone=request.POST["telephone"]
        province=request.POST["province"]
        district=request.POST["district"]
        address=request.POST["address"]
        number = request.POST["number"]
        size=request.POST["size"]
        colour=request.POST["colour"]
        payment_method=request.POST["payment_method"]
        product_id = 4
        models.Customer.objects.create(product_id=product_id, name=name,surname=surname,telephone=telephone,province=province,district=district,
                                       address=address,number=number,size=size,colour=colour,payment_method=payment_method,date=current_time)
        

        return redirect(reverse('website_app:order_success'))
    else:
        return render(request,'website_app/order_4.html')
    

@csrf_protect
def order_success(request):
      return render(request, 'website_app/order_success.html')


def info_1(request):
      return render(request, 'website_app/info_1.html')

def info_2(request):
      return render(request, 'website_app/info_2.html')

def info_3(request):
      return render(request, 'website_app/info_3.html')

def info_4(request):
      return render(request, 'website_app/info_4.html')

