from django import forms
from coureser.models.Actor import Actor
from coureser.models.Country import Country
from coureser.models.Genre import Genre


class SearchForm(forms.Form):
    q = forms.CharField(label="Название", required=False)
    genre = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Genre.objects.all(),
        required=False,
        label="Жанры"
    )
    country = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Country.objects.all(),
        required=False,
        label="Страны"
    )
    actor = forms.ModelMultipleChoiceField(
        widget=forms.SelectMultiple,
        queryset=Actor.objects.all().order_by('firstName'),
        required=False,
        label="Актеры"
    )
    year_from = forms.IntegerField(min_value=1930, max_value=2020, label="Год от", required=False, )
    year_to = forms.IntegerField(min_value=1930, max_value=2020, label="До", required=False, )
