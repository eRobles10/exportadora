from django.urls import path
from . import views
from .views import CreateOrderView, OrdersListView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('createOrder/', login_required(CreateOrderView.as_view()), name='createOrder'),
    path('orderList/', login_required(OrdersListView.as_view()), name='orderList'),
]
