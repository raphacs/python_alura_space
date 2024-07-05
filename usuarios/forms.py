from django import forms 

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Nome de Login", 
        max_length=100, 
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite seu nome de login',
                'class': 'form-control'
                }
        )
        )
    senha = forms.CharField(
        label="Senha", 
        max_length=70, 
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Digite sua senha',
                'class': 'form-control'
                }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label='Nome de Cadastro', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome de cadastro',
            }
        )
    )
    email=forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite o email valido',
            }
        )
    )

    senha_1=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        ),
    )

    senha_2=forms.CharField(
        label='Confirme sua senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha novamente',
            }
        ),
    )