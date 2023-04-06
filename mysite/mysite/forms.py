from django import forms
from tinymce.widgets import TinyMCE

class NewsletterForm(forms.Form):
    subject = forms.CharField()
    receivers = forms.CharField()
    message = forms.CharField(label="Email content")