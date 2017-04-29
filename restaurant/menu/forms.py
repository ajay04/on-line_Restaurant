from django import forms
from .models import Food, Review


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('name','description', 'cuisine', 'price')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content','value')
