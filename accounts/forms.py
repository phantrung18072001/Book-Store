from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Account

class RegistrationForm(UserCreationForm):
    """ name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    phone = forms.CharField(max_length=50)
    address = forms.CharField(max_length=500)
    birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'})) """

    class Meta:
        model = Account
        fields = ('username','name','email','phone','address','birth','password1','password2')

class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('name','email','phone','address','birth')
    
    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use' %account.email)

        
