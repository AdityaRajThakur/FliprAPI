from django.db import models
import uuid 
from django.http import Http404
# Create your models here.


#customer 

class Customer(models.Model):
    CustomerName = models.CharField(max_length=100) 
    Email = models.EmailField(max_length=254)
    MobileNumber= models.CharField(max_length=10) 
    City = models.CharField(max_length=100) 
    CustomerID = models.AutoField(primary_key=True) 
    def __str__(self) :
        return str(self.CustomerID)

#order 

class Order(models.Model):
    PurchaseID = models.UUIDField(unique=True ,default=uuid.uuid4, primary_key=True)
    ProductName = models.CharField(max_length=100) 
    Quantity = models.IntegerField() 
    Price = models.DecimalField(max_digits=10 , decimal_places=2) 
    MRP= models.DecimalField(max_digits=10 , decimal_places = 2) 
    CustomerID = models.ForeignKey(Customer , on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.Price < self.MRP:
            super(Order, self).save(*args, **kwargs)
        else: 
            raise Http404("Price of the Product is greater than MRP")

    def __str__(self) :
        return str(self.PurchaseID)

#shipping 

class Shipping(models.Model):
    Address = models.CharField(max_length=200) 
    Pincode = models.CharField(max_length=10) 
    City = models.CharField(max_length=100) 
    
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    PurchaseID = models.ForeignKey(Order , on_delete=models.CASCADE , null = True , blank=True)

    def __str__(self) -> str:
        return f"'{self.CustomerID.CustomerName}'-'{self.PurchaseID.ProductName}'"