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
def order(request):
    if request.POST:
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
        models.Customer.objects.create(name=name,surname=surname,telephone=telephone,province=province,district=district,
                                       address=address,number=number,size=size,colour=colour,payment_method=payment_method)
        

        return redirect(reverse('website_app:order_success'))
    else:
        return render(request,'website_app/order.html')
    
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
def order_5(request):
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
        product_id = 5
        models.Customer.objects.create(product_id=product_id, name=name,surname=surname,telephone=telephone,province=province,district=district,
                                       address=address,number=number,size=size,colour=colour,payment_method=payment_method,date=current_time)
        

        return redirect(reverse('website_app:order_success'))
    else:
        return render(request,'website_app/order_5.html')

@csrf_protect
def order_6(request):
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
        product_id = 6
        models.Customer.objects.create(product_id=product_id, name=name,surname=surname,telephone=telephone,province=province,district=district,
                                       address=address,number=number,size=size,colour=colour,payment_method=payment_method,date=current_time)
        

        return redirect(reverse('website_app:order_success'))
    else:
        return render(request,'website_app/order_6.html')

@csrf_protect
def order_7(request):
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
        product_id = 7
        models.Customer.objects.create(product_id=product_id, name=name,surname=surname,telephone=telephone,province=province,district=district,
                                       address=address,number=number,size=size,colour=colour,payment_method=payment_method,date=current_time)
        

        return redirect(reverse('website_app:order_success'))
    else:
        return render(request,'website_app/order_7.html')


@csrf_protect
def order_8(request):
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
        product_id = 8
        models.Customer.objects.create(product_id=product_id, name=name,surname=surname,telephone=telephone,province=province,district=district,
                                       address=address,number=number,size=size,colour=colour,payment_method=payment_method,date=current_time)
        

        return redirect(reverse('website_app:order_success'))
    else:
        return render(request,'website_app/order_8.html')


@csrf_protect
def order_9(request):
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
        product_id = 9
        models.Customer.objects.create(product_id=product_id, name=name,surname=surname,telephone=telephone,province=province,district=district,
                                       address=address,number=number,size=size,colour=colour,payment_method=payment_method,date=current_time)
        

        return redirect(reverse('website_app:order_success'))
    else:
        return render(request,'website_app/order_9.html')


@csrf_protect
def order_10(request):
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
        product_id = 10
        models.Customer.objects.create(product_id=product_id, name=name,surname=surname,telephone=telephone,province=province,district=district,
                                       address=address,number=number,size=size,colour=colour,payment_method=payment_method,date=current_time)
        

        return redirect(reverse('website_app:order_success'))
    else:
        return render(request,'website_app/order_10.html')


@csrf_protect
def order_11(request):
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
        product_id = 11
        models.Customer.objects.create(product_id=product_id, name=name,surname=surname,telephone=telephone,province=province,district=district,
                                       address=address,number=number,size=size,colour=colour,payment_method=payment_method,date=current_time)
        

        return redirect(reverse('website_app:order_success'))
    else:
        return render(request,'website_app/order_11.html')


@csrf_protect
def order_12(request):
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
        product_id = 12
        models.Customer.objects.create(product_id=product_id, name=name,surname=surname,telephone=telephone,province=province,district=district,
                                       address=address,number=number,size=size,colour=colour,payment_method=payment_method,date=current_time)
        

        return redirect(reverse('website_app:order_success'))
    else:
        return render(request,'website_app/order_12.html')

@csrf_protect
def size_table(request):
   	 return render(request,'website_app/size_table.html')

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


def info_5(request):
      return render(request, 'website_app/info_5.html')

def info_6(request):
      return render(request, 'website_app/info_6.html')

def info_7(request):
      return render(request, 'website_app/info_7.html')

def info_8(request):
      return render(request, 'website_app/info_8.html')


def info_9(request):
      return render(request, 'website_app/info_9.html')

def info_10(request):
      return render(request, 'website_app/info_10.html')

def info_11(request):
      return render(request, 'website_app/info_11.html')

def info_12(request):
      return render(request, 'website_app/info_12.html')
