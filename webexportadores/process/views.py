from django.shortcuts import render
from .models import Process

# Create your views here.


def process(request):
    process = Process.objects.all()
    return render(request, "process/process.html", {'processes': process})
