from django.contrib import admin
from .models import About

# Register your models here.
class AboutAdmin (admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display =  ('title','order')


admin.site.register(About, AboutAdmin)