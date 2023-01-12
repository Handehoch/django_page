from django import forms


class SkillForm(forms.Form):
    date_from = forms.DateField()
