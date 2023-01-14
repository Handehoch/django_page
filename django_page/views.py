import datetime
import json
from pathlib import PurePath

import pandas as pd
from django.http import HttpRequest
from django.shortcuts import render

from django_page.forms.vacancies_form import VacanciesForm
from django_page.forms.skills_form import SkillsForm
from django_page.models import Vacancy
from django_page.services.skills import SkillsService
from django_page.settings import BASE_DIR

ss = SkillsService()


def index(request: HttpRequest):
    return render(request, 'views/index.html', {
        'title': 'Fullstack разработчик'
    })


def demand(request: HttpRequest):
    df = pd.read_csv(PurePath(BASE_DIR) / 'django_page/data/years.csv')
    json_records = df.reset_index().to_json(orient='records')
    data = json.loads(json_records)
    
    context = {
        'title': 'Востребованность',
        'data': data
    }
    
    return render(request, 'views/demand.html', context)


def geography(request: HttpRequest):
    df = pd.read_csv(PurePath(BASE_DIR) / 'django_page/data/cities.csv')
    json_records = df.reset_index().to_json(orient='records')
    data = json.loads(json_records)
    
    context = {
        'title': 'География',
        'data': data
    }
    
    return render(request, 'views/geograpy.html', context)


def skills(request: HttpRequest):
    form = SkillsForm(request.POST)
    
    context = {
        'form': form,
        'title': 'Популярные навыки'
    }
    
    if form.is_valid():
        select = form.cleaned_data['select']
        df = pd.read_csv(PurePath(BASE_DIR) / f'django_page/data/result{select}.csv')
        json_records = df.reset_index().to_json(orient='records')
        skills_data = json.loads(json_records)
        context['skills'] = skills_data
    
    return render(request, 'views/skills.html', context)


def vacancies(request: HttpRequest):
    form = VacanciesForm(request.POST)
    
    vacancies_data: [Vacancy] = []
    if form.is_valid():
        date_from = form.cleaned_data['date_from']
        date_to = date_from + datetime.timedelta(days=1)
        vacancies_data: [Vacancy] = sorted([ss.get_vacancy(x.id) for x in ss.get_vacancies(date_from, date_to)],
                                           key=lambda x: x.published_at)
    
    context = {
        'form': form,
        'title': 'Последние вакансии',
        'vacancies': vacancies_data
    }
    
    return render(request, 'views/vacancies.html', context)
