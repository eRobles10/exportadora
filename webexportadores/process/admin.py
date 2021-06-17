from django.contrib import admin
from .models import Process


# Register your models here.
class ProcessAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'order')


admin.site.register(Process, ProcessAdmin)
