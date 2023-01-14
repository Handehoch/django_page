from django import forms


class VacanciesForm(forms.Form):
    date_from = forms.DateField()
