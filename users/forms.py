from django import forms
from users.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name","class_name", "division", "email", "username", "password"]
        widgets = {
            "password" : forms.widgets.PasswordInput(attrs ={
                "class":"hello", 
                "data_value":"123", 
                "placeholder":"Enter Strong Password"
                })
        }