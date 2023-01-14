import re


class Vacancy:
    def __init__(self, response_data):
        self.id: str = response_data['id']
        self.name: str = response_data['name']
        self.url: str = response_data['url'] if 'url' in response_data else response_data[
            'alternate_url'] if 'alternate_url' in response_data else None
        self.employer: Employer = Employer(response_data['employer'])
        self.salary: Salary = Salary(response_data['salary'])
        self.area: Area = Area(response_data['area'])
        self.published_at: str = response_data['published_at'].split('T')[0]
        self.key_skills: str = ', '.join(list(map(lambda vacancy: vacancy['name'], response_data[
            'key_skills']))) if 'key_skills' in response_data else None
        
        self.description = self._remove_html(response_data['description'])[
                           :150] + '...' if 'description' in response_data else None
    
    def _remove_html(self, query: str):
        html_cleaner = re.compile('<.*?>')
        cleantext = re.sub(html_cleaner, '', query)
        cleantext = re.sub(' +', ' ', cleantext)
        cleantext = re.sub(" ", " ", cleantext)
        cleantext = re.sub(" ", " ", cleantext)
        cleantext = self._strip_once(cleantext)
        cleantext = cleantext.split('\n')
        
        for i in range(len(cleantext)):
            cleantext[i] = re.sub(" +", " ", cleantext[i])
            cleantext[i] = self._strip_once(cleantext[i])
        
        return ', '.join(cleantext)
    
    @staticmethod
    def _strip_once(text):
        if text[0] == " ":
            text = text[1:]
        if text[-1] == " ":
            text = text[:-1]
        
        return text
    
    def __str__(self):
        return f'{self.id}\n{self.name}\n{self.url}\n{self.employer}\n{self.salary}\n{self.area}\n{self.published_at}\n{self.description}\n{self.key_skills}'


class Employer:
    def __init__(self, data):
        self.id: str = data['id']
        self.name: str = data['name']
        self.url: str = data['url']
    
    def __str__(self):
        return f'{self.id} {self.name} {self.url}'


class Salary:
    def __init__(self, data):
        if data is None:
            self.salary_from = None
            self.salary_to = None
            self.currency = None
            self.gross = None
            self.average_salary = None
            return
        
        self.salary_from: int = data['from']
        self.salary_to: int = data['to']
        self.currency: str = data['currency']
        self.gross: bool = data['gross']
        self.average_salary = self.__get_average_salary()
    
    def __get_average_salary(self):
        if self.salary_from is None and self.salary_to is None:
            return None
        elif self.salary_from is None:
            return self.salary_to
        elif self.salary_to is None:
            return self.salary_from
        else:
            return (self.salary_from + self.salary_to) // 2
    
    def __str__(self):
        return f'{self.salary_from} {self.salary_to} {self.average_salary} {self.currency} {self.gross}'


class Area:
    def __init__(self, data):
        self.id: str = data['id']
        self.name: str = data['name']
        self.url: str = data['url']
    
    def __str__(self):
        return f'{self.id} {self.name} {self.url}'
