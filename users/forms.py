from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Group,Permission
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
         

class AssignRoleForm(StyledFormMixin,forms.Form):
    role=forms.ModelChoiceField(
        queryset=Group.objects.all(),
        empty_label="Selected to Roll"
    )
    
        
# class CreateGroupForm(forms.ModelForm):
#         permissions=forms.ModelMultipleChoiceField (
#             queryset=Permission.objects.all(),
#             widget=forms.CheckboxSelectMultiple,
#             required=False,
#             label='Assign Permission'
            
#         )         
#         class Meta:
#             model=Group
#             fields=['name','permissions']

class create_from(StyledFormMixin, forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Assign Permission'
    )

    class Meta:
        model = Group
        fields = ['name', 'permissions']