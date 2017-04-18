from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Food, Review
from .forms import FoodForm, ReviewForm
from django.shortcuts import redirect
from django.db.models import Q



# Create your views here.

def index(request):
    context = { 'foods' : Food.objects.all()}
    return render(request, 'menu/index.html', context)

def cuisine(request, cuisine=None):
    foods = Food.objects.filter(cuisine=cuisine)
    context = {
                'name': cuisine,
                'foods' : foods
            }
    return render(request, 'menu/cuisine.html', context)

def food(request, cuisine=None, food=None):
    if request.method == 'POST':
        form = ReviewForm (request.POST or None)
        if form.is_valid():
            instance = Food.objects.get(name=request.POST.get('food'))
            instance.rateFood(request)
            instance.save()
            form.save()
            return redirect('menu:food', food=food, cuisine=cuisine)

    form = ReviewForm()
    instance = Food.objects.get(name=food)
    reviews = Review.objects.filter(food=food)
    context = {
                'food': instance,
                'reviews': reviews,
                'form' : form
                }
    return render(request, 'menu/food.html', context)


def createFood(request):
    if request.method == 'GET':
        form = FoodForm()
        return render (request, 'menu/create.html', {'form' : form})
    elif request.method == 'POST':
        form = FoodForm (request.POST or None)
        if form.is_valid():
            form.save()
            return render (request, 'menu/success.html')

def search(request):
    q = request.GET['q'].lower()
    results = Food.objects.filter(Q(description__icontains=q) |
                    Q(name__icontains=q) | Q(cuisine__icontains=q) ).order_by('-avg_rating')
    context = {'foods':results, 'term': q}
    return render (request,'menu/searchResults.html', context)
