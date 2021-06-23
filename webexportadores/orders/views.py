from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Order
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
from .forms import OrderForm

# Create your views here.


class CreateOrderView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateOrderView, self).form_valid(form)


class OrdersListView(ListView):
    template_name = "orders/order_list.html"
    model = Order

    def get_queryset(self, *args, **kwargs):
        staffUser = self.request.user.is_staff

        if staffUser:
            orders = Order.objects.filter()
        else:
            orders = Order.objects.filter(author=self.request.user)
        return orders
