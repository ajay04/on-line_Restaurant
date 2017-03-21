from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible
from registration.supplements.base import RegistrationSupplementBase

PROFILE_TYPES = (
        ('customer', 'customer'),
        ('chef', 'chef'),
        ('manager', 'manager'),
        ('delivery man', 'delivery man')
    )

class MyRegistrationSupplement(RegistrationSupplementBase):
	realname = models.CharField("Full Name", max_length=100, help_text="Please fill your real name")
	#age = models.IntegerField("Age")
	user_type = models.CharField(max_length=20, default='customer', choices=PROFILE_TYPES)
	remarks = models.TextField("Remarks", blank=True)
	address = models.TextField("Customer's address", max_length=200, blank=True )

	'''def __unicode__(self):
    	return unicode(self.realname)
	'''
	def __unicode__(self):
		return  "%s (%s) %s " % (self.realname, self.remarks,  self.user_type)
'''
def __str__ (self):
		# a summary of this supplement
	return self.realname
'''