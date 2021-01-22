from django import forms
from .models import Message

class ContactForm(forms.ModelForm):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Message
        fields = ('subject', 'email', 'message')
