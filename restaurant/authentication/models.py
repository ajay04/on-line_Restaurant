from __future__ import unicode_literals
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
PROFILE_TYPES = (
        ('customer', 'customer'),
        ('chef', 'chef'),
        ('manager', 'manager'),
        ('delivery man', 'delivery man')
    )

class UserProfile(models.Model):
	user = models.OneToOneField(User, primary_key=True, related_name='userprofile')
	user_type = models.CharField(max_length=20, default='customer', choices=PROFILE_TYPES)
	#location = models.CharField(max_length=40, null=True, blank=True)

def __str__(self):
	return self.user.username
'''

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
   
   '''
def create_profile(sender, **kwargs):
    """
    Basic user profile creation in database
    """
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)