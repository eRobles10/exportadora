from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(
        required=True, help_text="Requiered, Max 254 characters, valid email")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Entered email already registered, try with another.")

        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'rfc', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Name'}),
            'rfc': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'RFC'}),
            'phone': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Phone Number'})
        }
