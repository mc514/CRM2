from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
	name = models.CharField(max_length=20, null=True)
	
	def __str__(self):
	    return self.name

class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=18, null=True)
	email = models.EmailField(max_length=50, null=True)
	date_created = models.DateField(auto_now_add=True, null=True)
	
	def __str__(self):
	    return self.name

class Product(models.Model):

	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 

	name = models.CharField(max_length=200, null=True) # null=True with this we get error
	price = models.FloatField(null=True) 
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.TextField(max_length=500, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	tags = models.ManyToManyField(Tag)
	
	def __str__(self):
		return self.name
     

class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			) 

	customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, null=True)
	product = models.ForeignKey(Product, on_delete= models.SET_NULL, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return str(self.product)
