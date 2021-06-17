from django import forms
from .models import Post

class PageForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','intro','content', 'image', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'intro': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}), 
            'categories': forms.SelectMultiple(attrs={'class':'form-control'})
        }

