from django.contrib import admin
from .models import Certification

# Register your models here.


class CertificationAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = (str('title'), 'order')


admin.site.register(Certification, CertificationAdmin)
