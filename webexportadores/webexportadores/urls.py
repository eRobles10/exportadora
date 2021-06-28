"""webexportadores URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    # Django JET URLS
    #path('jet/', include('jet.urls', 'jet')),
    # paths core
    path('', include('core.urls')),
    path('news/', include('news.urls')),
    path('about/', include('about.urls')),
    path('certification/', include('certification.urls')),
    path('process/', include('process.urls')),
    path('admin/', admin.site.urls),
    path('orders/', include('orders.urls')),
    # paths de autenticacion
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]

urlpatterns += i18n_patterns(
    # Django JET URLS
    #path('jet/', include('jet.urls', 'jet')),
    # paths core
    path('', include('core.urls')),
    path('news/', include('news.urls')),
    path('about/', include('about.urls')),
    path('certification/', include('certification.urls')),
    path('process/', include('process.urls')),
    path('orders/', include('orders.urls')),
    # paths de autenticacion
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
)


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
