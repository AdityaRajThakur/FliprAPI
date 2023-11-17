from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from .models import Customer , Order , Shipping
from .serializers import CustomerSerializers , OrderSerializers , ShippingSerializers
# Create your views here.


@api_view(['GET']) 
def customers(request):
    data = Customer.objects.all() 
    # print(data) 
    Serialized_data = CustomerSerializers(data  ,many = True) 
    return Response(Serialized_data.data)   


@api_view(['POST']) 
def create_customer(request):
    data = request.data
    Serialized_data = CustomerSerializers(data = data, many = True)
    if(Serialized_data.is_valid()):
        Serialized_data.save() 
        # print(Serialized_data.initial_data)   
        return Response(Serialized_data.data)
    return Response(Serialized_data.errors) 

@api_view(['POST'])
def create_order(request):
    data = request.data 
    Serialized_data = OrderSerializers(data = data , many =True) 
    if(Serialized_data.is_valid()):
        Serialized_data.save() 
        return Response(Serialized_data.data) 
    return  Response(Serialized_data.errors) 


@api_view(['POST']) 
def create_shipping(request):
    data = request.data 
    Serialized_data = ShippingSerializers(data = data , many = True) 
    if(Serialized_data.is_valid()):
        Serialized_data.save() 
        return Response(Serialized_data.data) 
    return Response(Serialized_data.errors) 


@api_view(['GET'])
def customers_in_city(request):
    city = request.query_params.get('search')
    data = Shipping.objects.filter(City=city)
    customer_data = [cust.CustomerID.CustomerID for cust in data]
    serialized_data = CustomerSerializers(Customer.objects.filter(CustomerID__in = customer_data), many = True) 
    # print(serialized_data.data)
    return Response(serialized_data.data) 


@api_view(['GET'])
def customer_purchase_history(request):
    data = Customer.objects.all()
    lst =[] 
    for obj in data:
        orders_for_customer = Order.objects.filter(CustomerID = obj.CustomerID)
        dct = {
            "CustomerID":obj.CustomerName,
            "CustomerName":obj.CustomerName,
            "City":obj.City, 
            "Email":obj.Email,
            "PhoneNumber":obj.MobileNumber,
            "PurchaseOrder": OrderSerializers(orders_for_customer, many = True).data
            } 
        # print(type(OrderSerializers(orders_for_customer, many = True).data))
        lst.append(dct)

    return Response(lst)


@api_view(['GET']) 
def customer_shipping_history(request):
    data = Customer.objects.all()
    lst =[] 
    for obj in data:
        orders_for_customer = Order.objects.filter(CustomerID = obj.CustomerID)
        ships_for_customer = Shipping.objects.filter(CustomerID = obj.CustomerID) 
        dct = {
            "CustomerID":obj.CustomerName,
            "CustomerName":obj.CustomerName,
            "City":obj.City, 
            "Email":obj.Email,
            "PhoneNumber":obj.MobileNumber,
            "PurchaseOrder": OrderSerializers(orders_for_customer, many = True).data,
            "ShippingDetails" :ShippingSerializers(ships_for_customer,many = True).data
            } 
        lst.append(dct)
    return Response(lst) 


