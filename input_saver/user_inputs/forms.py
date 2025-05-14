from django import forms
from .models import UserInput


class InputForm(forms.ModelForm):
    class Meta:
        model = UserInput
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }
