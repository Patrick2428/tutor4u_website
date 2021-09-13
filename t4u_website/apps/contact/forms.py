from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, label='Name*' ,widget=forms.TextInput(attrs={'class':'form-control'}))
    grade = forms.CharField(required=True, label='Grade*', widget=forms.NumberInput(attrs={'class':'form-control'}))
    school = forms.CharField(required=True, label='School*', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True, label='Email*', widget=forms.EmailInput(attrs={'class':'form-control'}))
    phone = forms.CharField(required=False, label='Phone', widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(required=False, label='Message', widget=forms.Textarea(attrs={'class':'form-control', 'rows':10}))
