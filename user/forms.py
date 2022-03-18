from django import forms
from .models import User


class AddUserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'national_code', 'branch_code']

    def clean(self):
        cleaned_data = super(AddUserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")

        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(AddUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LogInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'txt', 'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'txt', 'placeholder': 'password'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username=username).first()
        if user is None:
            raise forms.ValidationError('user does not exist')
        return username
