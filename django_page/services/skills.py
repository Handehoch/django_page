import json
import requests

from django_page.models import Vacancy


class SkillsService:
    def __init__(self):
        self.base_url = 'https://api.hh.ru/vacancies'
        
    def get_vacancies(self, date_from: str, date_to: str) -> [Vacancy]:
        response = requests.get(f'{self.base_url}?text=fullstack&only_with_salary=true&per_page=10&date_from={date_from}&date_to={date_to}')
        response = list(map(Vacancy, json.loads(response.content.decode(encoding='utf-8-sig'))['items']))
        return response
    
    def get_vacancy(self, vacancy_id: int) -> Vacancy:
        response = requests.get(f'{self.base_url}/{vacancy_id}')
        return Vacancy(json.loads(response.content.decode(encoding='utf-8-sig')))
