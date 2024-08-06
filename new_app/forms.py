from django import forms

from new_app.models import Furniture


class furnitureForm(forms.ModelForm):
    class Meta:
        model = Furniture
        fields = ("__all__")