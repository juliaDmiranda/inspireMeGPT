from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.forms import TextInput, EmailInput

class InputForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'width: 300px;', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' :'Password', 'style': 'width: 300px;', 'class': 'form-control'}))

def validate_allowed_domains(value):
    allowed_domains = ['gmail.com', 'outlook.com']  # Specify the allowed domains here

    domain = value.split('@')[1] if '@' in value else None
    if domain not in allowed_domains:
        raise forms.ValidationError(f'Email address domain is not allowed.')
    
class SignUpForm(UserCreationForm):
    password2 = forms.CharField(
    label="Confirm  your Password",
    widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}), # remove talvez
    help_text=None,
    )

    password1 = forms.CharField(help_text=None)
    username = forms.CharField(
        help_text=None
    )
    email = forms.EmailField(validators=[validate_allowed_domains]) # remove talvez
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    # Add your custom validation logic here
    # def clean_password1(self):
    #     password1 = self.cleaned_data.get('password1')
    #     if len(password1) < 8:
    #         raise forms.ValidationError("Your password is too small. It must be at least 8 characters long.")
    #     return password1
    # fazer validação de email


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'style': 'width: 300px;', 'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'style': 'width: 300px;', 'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'style': 'width: 300px;', 'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'style': 'width: 300px;', 'class': 'form-control'})

class SignUpForm2(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Username', 'style': 'width: 300px;background-color:red;', 'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email', 'style': 'width: 300px;', 'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password', 'style': 'width: 300px;', 'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password', 'style': 'width: 300px;', 'class': 'form-control'})
