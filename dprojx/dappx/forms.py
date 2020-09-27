from django import forms
from django.db import models

from dappx.models import UserProfileInfo
from django.contrib.auth.models import User
from .models import Post,JsonFile
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')
class PostCreateForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('title','body','user_id')

class PostForm(forms.ModelForm):
    class Meta():
        model = JsonFile
        fields = ('file',)