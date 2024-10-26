from django import forms

class LoginForm(forms.Form):
    log_username = forms.CharField(max_length=100)
    log_password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    reg_username = forms.CharField(max_length=100)
    reg_password = forms.CharField(widget=forms.PasswordInput)
    reg_password2 = forms.CharField(widget=forms.PasswordInput)