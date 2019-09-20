from django import forms
from index.models import Expansion

import json

class ExpansionMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.name}'

class RotationRouletteForm(forms.Form):
    expansions = ExpansionMultipleChoiceField(
        queryset=Expansion.objects.all()
    )
    url = forms.CharField()
