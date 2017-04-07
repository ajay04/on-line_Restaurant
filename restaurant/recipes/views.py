from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Recipe, Review
from .forms import RecipeForm, ReviewForm
from django.shortcuts import redirect
from django.db.models import Q



# Create your views here.
def home(request):
    return redirect('recipes/')

def index(request):
    context = { 'recipes' : Recipe.objects.all()}
    return render(request, 'recipes/index.html', context)

def cuisine(request, cuisine=None):
    recipes = Recipe.objects.filter(cuisine=cuisine)
    context = {
                'name': cuisine,
                'recipes' : recipes
            }
    return render(request, 'recipes/cuisine.html', context)

def recipe(request, cuisine=None, food=None):

    if request.method == 'POST':
        form = ReviewForm (request.POST or None)
        if form.is_valid():
            id = request.POST.get('recipe')
            instance = Recipe.objects.get(id=id)
            instance.rateRecipe(request)
            instance.save()
            form.save()
            return redirect('recipes:recipe', food=food, cuisine=cuisine)

    form = ReviewForm()
    recipe = Recipe.objects.get(name=food)
    reviews = Review.objects.filter(recipe=recipe)
    context = {
                'recipe': recipe,
                'reviews': reviews,
                'form' : form
                }
    return render(request, 'recipes/recipe.html', context)


def createRecipe(request):
    if request.method == 'GET':
        form = RecipeForm()
        return render (request, 'recipes/create.html', {'form' : form})
    elif request.method == 'POST':
        form = RecipeForm (request.POST or None)
        if form.is_valid():
            form.save()
            return render (request, 'recipes/success.html')

def search(request):
    q = request.GET['q'].lower()
    results = Recipe.objects.filter(Q(description__icontains=q) |
                    Q(name__icontains=q) | Q(cuisine__icontains=q) ).order_by('-avg_rating')
    context = {'recipes':results, 'term': q}
    return render (request,'recipes/searchResults.html', context)
