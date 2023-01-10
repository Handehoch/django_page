from django.http import HttpRequest
from django.shortcuts import redirect


# Create your views here.
def index(request: HttpRequest):
    return redirect('/profession')
