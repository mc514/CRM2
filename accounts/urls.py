from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.home, name='home'),
    #---------------------------------Customer URLS---------------------------------------
    path('customers/',views.customer_list, name='customer_list'),
    path('customer/<str:pk>/',views.customer, name='customer'),
    # path('customers_detail/<str:pk>/',views.customers, name='customers'),

    path('products/',views.products, name='products'),
    path('create_order/<str:pk>/',views.createOrder, name='create_order'),
    path('update_order/<str:pk>',views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),


]