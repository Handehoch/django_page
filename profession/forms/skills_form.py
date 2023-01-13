from django import forms


class SkillsForm(forms.Form):
    CHOICES = (
        ('2015', '2015'), ('2016', '2016'),
        ('2017', '2017'), ('2018', '2018'),
        ('2019', '2019'), ('2020', '2020'),
        ('2021', '2021'), ('2022', '2022')
    )
    select = forms.ChoiceField(choices=CHOICES)
