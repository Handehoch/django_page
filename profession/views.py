import json
from pathlib import PurePath

import pandas as pd
from django.http import HttpRequest
from django.shortcuts import render

from django_page.settings import BASE_DIR
from profession.forms.vacancies_form import VacanciesForm
from profession.forms.skills_form import SkillsForm
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
    form = SkillsForm(request.POST)
    
    context = {
        'form': form,
        'title': 'Популярные навыки'
    }
    
    if form.is_valid():
        select = form.cleaned_data['select']
        df = pd.read_csv(PurePath(str(BASE_DIR) + f'/profession/data/result{select}.csv'))
        json_records = df.reset_index().to_json(orient='records')
        skills_data = json.loads(json_records)
        context['skills'] = skills_data
    
    return render(request, 'profession/views/skills.html', context)


def vacancies(request: HttpRequest):
    form = VacanciesForm(request.POST)
    
    vacancies_data: [Vacancy] = []
    if form.is_valid():
        date_from = form.cleaned_data['date_from']
        vacancies_data: [Vacancy] = sorted([ss.get_vacancy(x.id) for x in ss.get_vacancies(date_from)],
                                           key=lambda x: x.published_at)
    
    context = {
        'form': form,
        'title': 'Последние вакансии',
        'vacancies': vacancies_data
    }
    
    return render(request, 'profession/views/vacancies.html', context)
