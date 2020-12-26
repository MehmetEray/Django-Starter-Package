from django import forms

class RegisterForm(Forms.Form):
    username = forms.CharField(max_length=50,label = 'Kullanici Adi')
    password = forms.CharField(max_length=50,label = 'Sifre',widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=50,label = 'Yeniden sifreyi giriniz',widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("Username")
        password = self.cleaned_data.get("Password")
        confirm = self.cleaned_data.get("Confirm")

        
        