from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect


# Create your views here.
def index(request: HttpRequest):
	return redirect('/profession')
