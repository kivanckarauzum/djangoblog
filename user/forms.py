from django import forms

class RegisterForm(forms.Form):

    username = forms.CharField(max_length=20,label="Kullanıcı Adı")
    password = forms.CharField(max_length=16,min_length=3,widget= forms.PasswordInput,label="Parola ")
    repassword = forms.CharField(max_length=16,min_length=3,widget= forms.PasswordInput,label="Parola Tekrar")

    def clean(self):
        
        username= self.cleaned_data.get("username")
        password= self.cleaned_data.get("password")
        repassword= self.cleaned_data.get("repassword")

        if password and repassword and repassword!=password:
            raise forms.ValidationError("Parolalar uyuşmuyor.")
        
        values={
            "username":username,
            "password":password,
            "repassword":repassword
        }
        return values

class LoginForm(forms.Form):

    username= forms.CharField(label="Kullanıcı Adı")
    password= forms.CharField(label="Parola",widget= forms.PasswordInput)
    








