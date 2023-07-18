from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' :'Password','class': 'form-control'}))

def validate_allowed_domains(value):
    allowed_domains = ['gmail.com', 'outlook.com']

    domain = value.split('@')[1] if '@' in value else None
    if domain not in allowed_domains:
        raise forms.ValidationError(f'Email address domain is not allowed.')
    
class SignUpForm(UserCreationForm):
    username = forms.CharField( help_text=None)
    email = forms.EmailField(validators=[validate_allowed_domains]) # add validator 
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control','label':"Confirm  your Password"})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})