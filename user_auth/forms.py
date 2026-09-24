from django import forms
from .models import Users_data


class Users_dataForm(forms.ModelForm):
    class Meta:
        model = Users_data
        # fields = ['name', 'email', 'password']
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control container'}),  
            'email': forms.EmailInput(attrs={'class': 'form-control container'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control container'}),
        }

# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = Users_data
#         fields = ['email', 'password']
      