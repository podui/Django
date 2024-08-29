from django import forms
from django.contrib.auth.models import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):

    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "email")

    def __init__(self):
        self.cleaned_data = None

    def is_valid(self):
        pass

    def save(self):
        pass