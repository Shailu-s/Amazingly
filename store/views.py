from django.shortcuts import render
from .models import Product , Category
from django.http import HttpResponse
from .models import Customer
# Create your views here.

def index(request):
    categories = Category.objects.all()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.objects.filter(category = categoryID)
    else:
        products = Product.objects.all()
    data = {'products' : products ,'categories': categories }
    return render(request,'index_file.html',data)

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    postdata = request.POST
    first_name = postdata.get('first_name')
    last_name = postdata.get('last_name')
    phone = postdata.get('phone')
    email = postdata.get('email')
    password = postdata.get('password')

    customer = Customer(first_name = first_name, last_name = last_name , phone = phone,
                        email = email, password = password)
    customer.save()

    return HttpResponse ('Signup successfull')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == Customer.objects.get(email = email) and password == Customer.objects.get(password = password):
        return HttpResponse('login Successful')
    return HttpResponse('invalid login')





