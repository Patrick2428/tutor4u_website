from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .forms import ContactForm

def contact(request):

    if request.method == "GET":
        form = ContactForm()
    
    else:
        raise NotImplementedError

    return render(request, "contact.html", {"form": form})



