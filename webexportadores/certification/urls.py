from django.urls import path
from . import views

urlpatterns = [
    path('', views.certification, name="certification"),
]
