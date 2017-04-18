from django import forms
from .models import Food, Review


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
