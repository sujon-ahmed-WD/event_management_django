from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Group,Permission
from event.forms import StyledFormMixin
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm,SetPasswordForm
from phonenumber_field.formfields import PhoneNumberField

from users.models import CustomUser
# from models import CustomUser

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
        

class CustomPasswordChangeForm(StyledFormMixin,PasswordChangeForm):
    pass

class  CustomPasswordResetForm(StyledFormMixin,PasswordResetForm):
    pass

class CustomPasswordResetConfirmForm(StyledFormMixin,SetPasswordForm):
    pass
""" 
class EditProfile(StyledFormMixin,forms.ModelForm):
    class Meta:
        model= User
        fields=['email','first_name','last_name']
        
    profile_image=forms.ImageField(required=False)
    phone = PhoneNumberField(region="BD")
    
    def __init__(self, *args, **kwargs):
        self.userprofile=kwargs.pop('userprofile',None)
        super().__init__(*args, **kwargs)
        print("forms",self.userprofile)
        
    def save(self,commit=True):
        user=super().save(commit=False)
        
        if self.userprofile:
            print("userprofile",userprofile.profile_image)
            
            self.fields['profile_image'].initial=self.userprofile.profile_image
            self.fields['phone'].initial=self.userprofile.phone
            
            if commit:
                print("userprofile",userprofile.profile_image)
                self.userprofile.save()
        if commit:
            user.save()
        
        return user
                
    """

class EditProfileForm(StyledFormMixin,forms.ModelForm):
        class Meta:
            model =CustomUser
            fields=['email','first_name','last_name','profile_image','phone']