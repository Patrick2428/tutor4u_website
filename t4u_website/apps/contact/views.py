from django import forms
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.mail import send_mail
import bleach 

from t4u_website import settings

from .forms import ContactForm

def contact(request: HttpRequest) -> HttpResponse:

    if request.method == "GET":
        form = ContactForm()
    
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = bleach.clean(form.cleaned_data["name"])
            grade = bleach.clean(form.cleaned_data["grade"])
            school = bleach.clean(form.cleaned_data["school"])
            email = bleach.clean(form.cleaned_data["email"])
            phone = bleach.clean(form.cleaned_data["phone"])
            message = bleach.clean(form.cleaned_data["message"])

            send_mail(f"{name} from {school} in grade {grade} sent an email - TELL: {phone}", message, email, [settings.DEFAULT_FROM_EMAIL])
            return render(request, "contact.html", {"form": form, "success": True})
    else:
        raise NotImplementedError

    return render(request, "contact.html", {"form": form})



