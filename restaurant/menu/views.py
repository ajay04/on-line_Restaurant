from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Food, Review, Order
from .forms import FoodForm, ReviewForm
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required


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


def getUserType(user):
    userType = 'VISITOR'
    if user.is_superuser:
        userType = 'MANAGER'
    try:
        if user.staff.user_type == 'CHEF':
            userType = 'CHEF'
        else:
            userType = 'DELIVERY'
    except:
        try:
            if user.customer.user_type == 'CUSTOMER':
                userType = 'CUSTOMER'
        except:
            pass
    return userType


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

@login_required  # TODO: Configure redirection after successful login
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
                    Q(name__icontains=q) |
                     Q(cuisine__icontains=q) ).order_by('-avg_rating')
    context = {'foods':results, 'term': q}
    return render (request,'menu/searchResults.html', context)

@login_required
def addToCart(request,food):
    user = request.user
    userType = getUserType(user)
    if userType != 'CUSTOMER':
        return

    instance = Order()
    instance.food = Food.objects.get(name=food)
    instance.customer = request.user
    instance.save()

#Fired form user cart:
def placeOrder(request):
    discount = 0.1
    customer = request.user
    orders = Order.filter(customer=customer,
                status='cart').order_by('time_stamp')
    total_price = 0.0
    num_orders = 0
    for order in orders:
        for i in range (order.quantity):
            total_price += order.food.price
            num_orders += 1
            order.food.numOrders +=1

    if (total_price > customer.balance):
        print ("Insufficient Funds")
        return
    if customer.is_vip:
        total_price *= (1-discount)
    customer.spending += total_price
    customer.numOrders += num_orders
    customer.balance -= total_price
    customer.check_satus()
    customer.save()
    for order in orders:
        order.status = 'pending'
        order.food.save()
        order.save()
