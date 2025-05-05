# forms.py
from django import forms
from .models import Contact

class MessageForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'message', 'email']
        widgets = {
            'message': forms.Textarea(attrs={'placeholder': 'رسالتك', 'rows': 7}),
            'email': forms.EmailInput(attrs={'placeholder': 'الايميل الخاص بك'}),
        }
