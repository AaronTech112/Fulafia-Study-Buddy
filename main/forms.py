from dataclasses import fields
from django.forms import ModelForm
from .models import Room, User, Message
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username', 'email','grade','password1', 'password2']

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants','grade']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','name','username', 'email', 'bio', 'grade',]
        
class UpdateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','name','username', 'email', 'bio', ]

class MessageImage(ModelForm):
    class Meta:
        model = Message
        fields = ['body','body_image']
