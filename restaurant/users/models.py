from django.db import models
from django.contrib.auth.models import User
from menu.models import models as menuModels


type_choices = (('CHEF', 'CHEF'), ('DELIVERY', 'DELIVERY'))


class Customer(models.Model):
    user = models.OneToOneField(User, related_name='customer')
    user_type = models.CharField(max_length=10, default='CUSTOMER')
    is_vip = models.BooleanField(default=False)
    balance = models.FloatField()
    numOrders = models.PositiveIntegerField(default=0)
    spending = models.PositiveIntegerField(default=0)
    is_approved = models.BooleanField(default=False)

    def check_status(self):
        if self.numOrders == 50 or self.spending >= 500 :
            self.is_vip = True

    def __str__(self):
	    return (self.user.first_name + self.user.last_name)


class Staff(models.Model):
    user = models.OneToOneField(User, related_name='staff')
    user_type = models.CharField(max_length =10,choices=type_choices)
    salary = models.FloatField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return (self.user.first_name + self.user.last_name)
