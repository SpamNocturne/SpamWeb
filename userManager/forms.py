from django import forms

class ConnexionForm(forms.Form):
    error_css_class = 'error text-red'
    required_css_class = 'required'
    username = forms.CharField(label="Pseudo", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


    def __init__(self, *args, **kwargs):
        super(ConnexionForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs\
            .update({
                'placeholder': "Pseudo",
                'class': 'form-control'
            })
        self.fields['password'].widget.attrs\
            .update({
                'placeholder': "Mot de passe",
                'class': 'form-control'
            })
