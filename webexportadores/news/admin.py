from django.contrib import admin
from .models import Blog, Category, Post


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields  = ('created','updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields  = ('created','updated')
    list_display =  ('title','author','created')



class BlogAdmin(admin.ModelAdmin):
    readonly_fields  = ('created','updated')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)