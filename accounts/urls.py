from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.home, name='home'),
    path('customer',views.customer, name='customer'),
    path('product',views.product, name='product'),

]