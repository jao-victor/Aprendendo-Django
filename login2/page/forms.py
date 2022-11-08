from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class LoginUser(forms.Form):

    username = forms.CharField(label='username', min_length=5, max_length=150)
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)



class CadastroUser(UserCreationForm):

    username = forms.CharField(label='username', min_length=5, max_length=150)
    email = forms.EmailField(label='email', required=True)
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    """class Meta:
        model = User
        fields = ['username', 'password1', 'password2']"""

    def username_clean(self):
        #verifica se o usuário já existe e, se exitir,
        #mostra uma mensagem de erro na hora

        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username = username).count()

        if new:
            raise ValidationError('Esse usuário já existe...')
        return username

    def email_clean(self):
        #verifica se o email já existe e, se exitir,
        #mostra uma mensagem de erro na hora

        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email).count()
        if new:
            raise ValidationError("Esse email já existe...")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit = True):
        user = User.objects.create_user(
        self.cleaned_data['username'],
        self.cleaned_data['email'],
        self.cleaned_data['password1']
        )



        return user
