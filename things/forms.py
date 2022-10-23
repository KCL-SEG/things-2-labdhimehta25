"""Forms of the project."""
from django import forms
from .models import Thing

# Create your forms here.
class ThingForm(forms.NOdelForm):
    class Meta:
        model = Thingsfiels = {'name', 'description', 'quantity'}
        widgets = {'description': forms.Textarea(), 'quantity': forms.NumberInput()}
