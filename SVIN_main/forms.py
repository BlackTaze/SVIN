from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Review
class RegisterUserForm(UserCreationForm):
	username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class':"form-input"}))
	password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class':"form-input"}))
	password2 = forms.CharField(label="Повтори пароль", widget=forms.PasswordInput(attrs={'class':"form-input"}))
    
	class Meta:
		model = User
		fields = ("username", "password1", 'password2')
		widjets = {
			"username" : forms.TextInput(attrs={'class':"form-input"}),
			"password1" : forms.PasswordInput(attrs={'class':"form-input"}),
			"password2" : forms.PasswordInput(attrs={'class':"form-input"})
		}
  
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance
        