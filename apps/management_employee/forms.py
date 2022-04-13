from django import forms


class LoginForms(forms.Form):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Usuário"}
        ),
    )
    password = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Senha"}
        ),
    )


class LogStatus(forms.Form):
    notes = forms.CharField(
        max_length=50,
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Notes"}),
    )


class RegisterForms(forms.Form):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Usuário"}
        ),
    )
    password = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Senha"}
        ),
    )
    # recovery_answer = forms.CharField(max_length=30,
    #                                   widget=forms.TextInput(
    #                                       attrs={'class': 'form-control', 'placeholder': 'Recovery Answer'}))
    recovery_email = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "E-mail de Recuperação"}
        ),
    )
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Primeiro Nome"}
        ),
    )
    middle_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nome do Meio"}
        ),
    )
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Sobrenome"}
        ),
    )
    department = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Departamento"}
        ),
    )
    phone_number = forms.IntegerField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Número de telefone"}
        )
    )
