from django import forms


class CommentForm(forms.Form):
    text = forms.CharField(
        label="Напишите что-нибудь",
        required=False,
        widget=forms.Textarea(attrs={'rows': '5'})
    )

