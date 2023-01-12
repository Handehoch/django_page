import json
from pathlib import PurePath

import pandas as pd
from django.http import HttpRequest
from django.shortcuts import render

from django_page.settings import BASE_DIR
from profession.forms.skills_form import SkillForm
from profession.models import Vacancy
from profession.services.skills import SkillsService

ss = SkillsService()


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
    form = SkillForm(request.POST)
    
    vacancies: [Vacancy] = []
    if form.is_valid():
        date_from = form.cleaned_data['date_from']
        vacancies: [Vacancy] = sorted([ss.get_vacancy(x.id) for x in ss.get_vacancies(date_from)],
                                      key=lambda x: x.published_at)
    
    context = {
        'form': form,
        'title': 'Последние вакансии',
        'vacancies': vacancies
    }
    
    return render(request, 'profession/views/skills.html', context)
