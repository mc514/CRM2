from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

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

#---------------------------------Customer Views---------------------------------------

def customer(request, pk):
    # return HttpResponse("Customer Page")
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()
    order_count = orders.count()

    context = {'customer': customer, 'orders': orders, 'order_count': order_count}
    return render(request, 'accounts/customer.html',context)

def customer_list(request):
    # return HttpResponse("Customer Page")
    customers = Customer.objects.all()
    return render(request, 'accounts/customer_list.html',{'customers':customers})

#---------------------------------Product Views---------------------------------------

def products(request):
    # return HttpResponse("Product Page")
    products = Product.objects.all()
    return render(request, 'accounts/products.html',{'products': products})

#-------------------(CREATE ORDER VIEWS) -------------------

def createOrder(request,pk):
	action = 'create'
	customer = Customer.objects.get(id=pk)
	form = OrderForm(initial={'customer': customer})
	if request.method == 'POST':
        # print('Printng POST:',request.POST)
		form = OrderForm(request.POST)
	
		if form.is_valid():
			form.save()
			return redirect('/')

	context =  {'form':form}
	return render(request, 'accounts/order_form.html', context)

#-------------------(UPDATE ORDER VIEWS) -------------------

def updateOrder(request,pk):
	action = 'update'
	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)
	if request.method == 'POST':
    # print('Printng POST:',request.POST)
		form = OrderForm(request.POST, instance=order)
	
		if form.is_valid():
			form.save()
			return redirect('/')

	context =  {'form':form}
	return render(request, 'accounts/order_form.html', context)

#-------------------(DELETE VIEWS) -------------------
def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == 'POST':
		order.delete()
		return redirect('/')
		
	return render(request, 'accounts/delete_item.html', {'item':order})