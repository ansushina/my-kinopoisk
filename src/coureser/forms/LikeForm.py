from django import forms


class LikeForm(forms.Form):
    value = forms.ChoiceField(
        choices=(
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5')
        ),
        label="Оцените фильм",
        required=False,
        widget=forms.RadioSelect,
    )