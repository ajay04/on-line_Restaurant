from django.db import models
from django.contrib.auth.models import User

# Create your models here.

USER_TYPE = (
        ('Customer', 'Customer'),
        ('Chef', 'Chef'),
        ('Manager', 'Manager'),
        ('elivery man', 'Delivery man')
        )

#following is our custom model
class UserProfile(models.Model):
#link our user with djano auth's User
	user = models.OneToOneField(User)
	name = models.CharField(max_length=30, )
	user_type = models.CharField(max_length=10, choices=USER_TYPE)
	vip_user = models.BooleanField("VIP User", editable=True, default=False)
	is_active = models.BooleanField('Active User', default = False)

	def __unicode__(self):
	    return (self.user.username)