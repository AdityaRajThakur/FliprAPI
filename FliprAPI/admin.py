from django.contrib import admin
from .models import Customer , Order , Shipping


# Register your models here.

@admin.register(Customer) 

# customer
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['CustomerName' , 'Email','City','CustomerID']

@admin.register(Order) 
# #order 
class OrderAdmin(admin.ModelAdmin):
    list_display = ['ProductName','Quantity' , 'Price', 'PurchaseID','CustomerID']


@admin.register(Shipping)
#Shipping
class ShippingAdmin(admin.ModelAdmin):
    list_display = ['Address','CustomerID','PurchaseID']