from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput())
    grade = forms.CharField(required=True, widget=forms.NumberInput())
    email = forms.EmailField(required=True, widget=forms.EmailInput())
    phone = forms.CharField(required=False, widget=forms.TextInput())
    message = forms.CharField(required=True, widget=forms.Textarea())
