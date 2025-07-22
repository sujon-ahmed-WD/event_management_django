
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from event.forms import StyledFormMixin
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(StyledFormMixin,UserCreationForm):
    class Meta:
          model = User
          fields=['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
          
    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         
    
         for fieldname in  self.fields:
             self.fields[fieldname].help_text=None
             
class LoginForm(StyledFormMixin,AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
         