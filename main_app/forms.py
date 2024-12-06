from django import forms
from .models import Feeding


class FeedingForm(forms.ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal'] # meals is limited ot breakfast, lunch, dinner as it was on models.py
        widgets = {
            'date': forms.DateInput( # Turns date into a proper date field
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }
