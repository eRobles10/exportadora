from django.shortcuts import render
from .models import Certification

# Create your views here.


def certification(request):
    certification = Certification.objects.all()
    return render(request, "certification/certifications.html", {'certification': certification})
