from django.shortcuts import render, HttpResponse
from process.models import Process
from news.models import Blog, Post
from certification.models import Certification
from about.models import About
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from django.shortcuts import render
# Create your views here.
"""
Inicio
Acerca de
Contacto
Beneficios
Blog
Servicios

"""


class HomePageView(TemplateView):

    template_name = "core/home.html"
    news = ""
    certification = get_object_or_404(Certification, order=0)
    process_intro = get_object_or_404(Process, pk=1)
    """Process.objects.get()"""
    about = get_object_or_404(About, order=0)

    def get(self, request, **kwargs):

        return render(request,
                      self.template_name, {'news': self.news,
                                           'certification': self.certification,
                                           'process_intro': self.process_intro,
                                           'about': self.about})


def contact(request):
    return render(request, "core/contact.html")
