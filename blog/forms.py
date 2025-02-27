from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Post
from django.core.validators import FileExtensionValidator
from django_ckeditor_5.widgets import CKEditor5Widget


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # profile_image = forms.ImageField()
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {'email':'Email ID', 'first_name':'First Name', 'last_name':'Last Name'}
        
        widgets = { 
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
        }

# class ProfileImageForm(forms.ModelForm):
#     profile_image = forms.ImageField(
#         required=False,
#         validators=[
#             FileExtensionValidator(
#                 allowed_extensions=['jpg', 'jpeg', 'png']
#                 )
#             ],
#         widget=forms.FileInput(attrs={'class':'form-control'})
#     )
#     class Meta:
#         model = User
#         fields = ['profile_image']
#         labels = {'profile_image':'Profile Image'}



class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'class':'form-control', 'autocomplete':'current-password'}))

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields["description"].required = False
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'author', 'description', 'image']
        labels = {'title':'Title', 'subtitle':'Subtitle', 'author':'Author', 'description':'Description', 'image':'Image'}
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'subtitle': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            "description": CKEditor5Widget(attrs={"class": "django_ckeditor_5"}, config_name="extends")
        }   

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = ['first_name', 'last_name', 'mobile', 'address', 'email', 'message']
#         labels = {'first_name':'First Name', 'last_name':'Last Name', 'mobile':'Mobile', 'address':'Address', 'email':'Email ID', 'message':'Message'}
#         widgets = {
#             'first_name': forms.TextInput(attrs={'class':'form-control'}),
#             'last_name': forms.TextInput(attrs={'class':'form-control'}),
#             'mobile': forms.TextInput(attrs={'class':'form-control'}),
#             'address': forms.TextInput(attrs={'class':'form-control'}),
#             'email': forms.EmailInput(attrs={'class':'form-control'}),
#             'message': forms.Textarea(attrs={'class':'form-control'}),
#         }