from django.forms import ModelForm
from .models import User, Account

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'department', 'role']

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['email','password']

