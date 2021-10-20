from autoslug import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password1',
            'password2'
        ]

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = [
            'profile_pic',
            'bio',
            'beginn',
            'end',
            'birthdate',
            'nickname',
            'img_1',
            'img_2',
            'img_3',
            'vid_1'
        ]
