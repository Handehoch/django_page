from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest):
	return render(request, 'profession/views/index.html', {
		'title': 'Fullstack разработчик'
	})


def demand(request: HttpRequest):
	return render(request, 'profession/views/demand.html')
