from django import forms

from . import models


class ReviewsAdd(forms.Form):
    CHOICE = [
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5')
    ]
    review = forms.ChoiceField(label='評価',widget=forms.RadioSelect,choices=CHOICE)
    class Meta:
        contents = ['review']