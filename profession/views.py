import os
import json
import pandas as pd

from pathlib import Path, PurePath
from django.http import HttpRequest
from django.shortcuts import render
from django_page.settings import BASE_DIR


# Create your views here.
def index(request: HttpRequest):
    return render(request, 'profession/views/index.html', {
        'title': 'Fullstack разработчик'
    })


def demand(request: HttpRequest):
    df = pd.read_csv(PurePath(str(BASE_DIR) + '/profession/data/years.csv'))
    json_records = df.reset_index().to_json(orient='records')
    data = json.loads(json_records)
    
    context = {
        'title': 'Востребованность',
        'data': data
    }
    
    return render(request, 'profession/views/demand.html', context)


def geography(request: HttpRequest):
    df = pd.read_csv(PurePath(str(BASE_DIR) + '/profession/data/cities.csv'))
    json_records = df.reset_index().to_json(orient='records')
    data = json.loads(json_records)
    
    context = {
        'title': 'География',
        'data': data
    }
    
    return render(request, 'profession/views/geograpy.html', context)


def skills(request: HttpRequest):
    return render(request, 'profession/views/skills.html')
