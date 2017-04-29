from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Food, Review
from .forms import FoodForm, ReviewForm
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.template import RequestContext 



def index(request):
#getting user type
    user = request.user
    user_type = 'visitor'
    if user.is_superuser:
        user_type == 'manager'
    try:
        if user.staff.user_type == 'CHEF':
            user_type = 'chef'
        else:
            user_type = 'delivery'
    except:
        try:
            if user.customer.user_type == 'CUSTOMER':
                user_type = 'customer'
            
        except:
            pass       
#getting food form
    if request.method == "POST":
        food_form = FoodForm(request.POST)
        if food_form.is_valid():
            food  = food_form.save(commit=False)
            food.chef = request.user
            food.save()
    else:
        food_form = FoodForm()
    context = {'food_item' : Food.objects.all(),
                'user_type': user_type,
                'food_form': food_form,
            }
    return render(request, 'users/index.html', context)

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

@login_required  # configure redirection after successful login
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
