from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#Registration Form

class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']