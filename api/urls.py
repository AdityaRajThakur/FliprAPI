from FliprAPI.views import (
    customers,
    create_customer , 
    create_order,
    create_shipping,
    customers_in_city,
    customer_purchase_history,
    customer_shipping_history
)
from django.urls import path  

urlpatterns = [
    path('customers', customers, name='get_customer_list'),
    path('create_customers', create_customer, name='create_customer'),
    path('create_orders', create_order, name='create_order'),
    path('create_shippings', create_shipping, name='create_shipping'),
    path('customers_in_city/', customers_in_city, name='get_customers_in_city'),
    path('customers_purchase_history', customer_purchase_history, name='get_customer_purchase_history'),
    path('customers_shipping_history', customer_shipping_history, name='get_customer_shipping_history'),
]
