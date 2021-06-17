from django.contrib import admin
from .models import Certification

# Register your models here.


class CertificationAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'order')


admin.site.register(Certification, CertificationAdmin)
