from django.urls import path
from .views import HomePageView
from . import views 

urlpatterns = [

    #paths de core
    path('', HomePageView.as_view(), name="home"),
    path('contact/', views.contact, name="contact"),
]
