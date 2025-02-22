from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("Home Page")
    return render(request, 'accounts/dashboard.html')
def customer(request):
    # return HttpResponse("Customer Page")
     return render(request, 'accounts/customer.html')
def products(request):
    # return HttpResponse("Product Page")
    return render(request, 'accounts/products.html')