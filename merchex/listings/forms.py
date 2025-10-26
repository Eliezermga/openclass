from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False, label="Votre nom")
    email = forms.EmailField(label="Votre email")
    message = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        label="Votre message"
    )