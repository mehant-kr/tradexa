from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User, Post

class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'username')

    def save(self, commit=True):
        user = super(UserCreateForm ,self).save(commit=False)
        if commit:
            user.save()
        return user


class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('user', 'text')

    def save(self, commit=True):
        user = super(PostCreateForm ,self).save(commit=False)
        if commit:
            user.save()
        return user