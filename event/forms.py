from django import forms
from .models import Event, Category



""" Mixing Django forms with Tailwind CSS for styling """
class StyledFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styles_widget()
        
    default_classes = "border border-gray-300 w-full p-3  rounded-lg shadow-sm focus:border-rose-500 focus:ring-rose-500"
    def apply_styles_widget(self):
        for field_name , field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f"Enter {(field.label or 'this field').lower()}"
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f"Enter {(field.label or 'this field').lower()}"
                })
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f"Select {(field.label or 'this field').lower()}"
                })
            elif isinstance(field.widget, forms.EmailInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f"Enter {(field.label or 'this field').lower()}"
                })
            elif isinstance(field.widget,forms.PasswordInput):
                field.widget.attrs.update({
                    'class':self.default_classes,
                    'placeholder': f"Select {(field.label or 'this field').lower()}"

                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                print("Inside Date")
                field.widget.attrs.update({
                    "class": "border-2 border-gray-300 p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                    field.widget.attrs['class'] = 'space-y-2'

class EventForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time', 'location', 'category']
        widgets ={
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-input'}),
            
        }
        
    def __init__(self, *arg, **kwarg):
      super().__init__(*arg, **kwarg)
      self.apply_styles_widget()

# class ParticipantForm(StyledFormMixin, forms.ModelForm):
#     class Meta:
#         model = Participant
#         fields = ['name', 'email', 'events']

#     def __init__(self, *arg, **kwarg):
#         super().__init__(*arg, **kwarg)
#         self.apply_styles_widget()

class CategoryForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea'}),
            
        }
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.apply_styles_widget()