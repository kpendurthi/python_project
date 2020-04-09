from django import forms
from .models import Houses, City

class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ('name',)

class HouseForm(forms.ModelForm):

    class Meta:
        model = Houses
        fields = ('name', 'address','amt','image_url', 'description', 'city',)