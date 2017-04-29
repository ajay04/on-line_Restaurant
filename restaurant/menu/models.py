from django.db import models

# Create your models here.
from django.db import models
from django.core.urlresolvers import reverse
from users import models as userModels


class Food(models.Model):
    name = models.CharField(max_length=100,blank=False)
    description = models.TextField(blank=False)
    price = models.PositiveIntegerField(blank=False)
    chef = models.ForeignKey(userModels.User)
    cuisine = models.CharField(max_length=100, default='')
    # customers = models.ManyToManyField(userModels.Customer)
    numOrdered = models.IntegerField(default=0)
    avg_rating = models.PositiveIntegerField(default=0)
    num_reviews = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ('menu:food',
         kwargs={'food':self.name, 'cuisine':self.cuisine} )

    def rateFood(self,request):
        rating = int(request.POST['value'])
        self.avg_rating = (self.num_reviews * self.avg_rating +
                                    rating) / (self.num_reviews+1)
        self.num_reviews +=1


class Order(models.Model):
    food = models.ForeignKey(Food)
    customer = models.ForeignKey(userModels.User, related_name='orders')
    status = models.CharField(max_length=10, default='cart')
    delivery = models.ForeignKey(userModels.User, related_name ='deliveries')
    time_stamp = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)
    def increment(self):
        self.quantity +=1


class Review(models.Model):
    content = models.TextField()
    value = models.PositiveIntegerField()
    author = models.ForeignKey(userModels.User)
    food = models.ForeignKey(Food)

class Message (models.Model):
    target = models.ForeignKey(userModels.User, related_name='inbox')
    issued_by = models.ForeignKey(userModels.User, related_name='outbox')
    reason = models.TextField()
    message_type = models.CharField(max_length=10)
