from django.db import models
from django.core.urlresolvers import reverse


class Chef(models.Model):
    name = models.CharField(max_length=100, blank=False)
    complaints = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100, blank=False)
    status = models.CharField(max_length=50, blank=False)
    is_VIP = models.BooleanField(default=True)
    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100,blank=False)
    description = models.TextField(blank=False)
    price = models.PositiveIntegerField(blank=False)
    chef = models.ForeignKey(Chef)
    cuisine = models.CharField(max_length=100, default='')
    customers = models.ManyToManyField(Customer)
    avg_rating = models.PositiveIntegerField(default=0)
    num_reviews = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ('menu:food', kwargs={'food':self.name, 'cuisine':self.cuisine} )

    def rateFood(self,request):
        rating = int(request.POST['value'])
        self.avg_rating = (self.num_reviews * self.avg_rating +
                                    rating) / (self.num_reviews+1)
        self.num_reviews +=1

class Review(models.Model):
    content = models.TextField()
    value = models.PositiveIntegerField()
    author = models.ForeignKey(Customer)
    food = models.ForeignKey(Food)
