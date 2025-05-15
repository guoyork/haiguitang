from django import forms
from .models import UserInput, Rating


class InputForm(forms.ModelForm):
    class Meta:
        model = UserInput
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score']
        widgets = {
            'score': forms.NumberInput(attrs={
                'type': 'range',
                'min': '1',
                'max': '5',
                'step': '1',
                'class': 'rating-slider',
                'id': 'ratingInput'
            })
        }