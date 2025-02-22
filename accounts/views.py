from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    # return HttpResponse("Home Page")
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()

    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()

    context = {'orders': orders, 'customers': customers, 
               'total_customers': total_customers, 'total_orders': total_orders,
               'delivered': delivered, 'pending': pending}
    return render(request, 'accounts/dashboard.html', context)

def customer(request):
    # return HttpResponse("Customer Page")
     return render(request, 'accounts/customer.html')
def products(request):
    # return HttpResponse("Product Page")
    products = Product.objects.all()
    return render(request, 'accounts/products.html',{'products': products})