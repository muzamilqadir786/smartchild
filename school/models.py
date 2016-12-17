from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
LEVEL = (
 	('Playgroup','Playgroup'),
 	('Nursery', 'Nursery'),
 	('PREP', 'PREP'),
 	('1st Grade', '1st Grade'),
 	('2nd Grade', '2nd Grade'),
 	('3rd Grade', '3rd Grade'),
 	('4th Grade', '4th Grade'),
)

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
)

mobilink = [x for x in range(300,310)]
zong = [x for x in range(310,316)]
warid = [x for x in range(320,325)]
ufone = [x for x in range(331,338)]
telenor = [x for x in range(340,350)]

mobile_codes = mobilink + zong + warid + ufone + telenor
mobile_codes = [(str(x).zfill(4), str(x).zfill(4)) for x in mobile_codes]

# import ipdb
# ipdb.set_trace()

class Level(models.Model):
	level = models.CharField(max_length=30,choices=LEVEL)
	def __unicode__(self):
		return self.get_level_display()

class Student(models.Model):
	first_name = models.CharField(max_length=30,blank=True,null=True)
	last_name = models.CharField(max_length=30,blank=True,null=True)
	father_name = models.CharField(max_length=30,blank=True,null=True)
	mother_name = models.CharField(max_length=30,blank=True,null=True)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='M')
	level = models.ForeignKey(Level,blank=True)
	mobile_code = models.CharField(max_length=4,choices=mobile_codes,default='0300')
	seven_digit_phone = models.CharField(max_length=7,blank=True,null=True)
	address = models.CharField(max_length=200,blank=True,null=True)
	date_of_birth = models.DateField(default='1/1/2000')
	# def __unicode__(self):
	# 	return "%s %s %s" % (self.id, self.first_name, self.last_name)
	def __str__(self):
		return "%s %s" % (self.first_name, self.last_name)


FEE_CATEGORY = (
			('M', 'Monthly_Fee'),
			('A', 'Admission_Fee'),
		)
class FeeCategory(models.Model):
	fee_category = models.CharField(max_length=30,blank=True,null=True)
	fee_amount = models.DecimalField(max_digits=6, decimal_places=2)
	description = models.TextField()
	slug = models.SlugField(blank=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.fee_category)
		super(FeeCategory, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s" % self.fee_category
	class Meta:
		verbose_name = 'Fee Categories'
		ordering = ('id',)

import calendar
MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1,13)]
class Fee(models.Model):
	# level = models.ForeignKey(Level)
	student = models.ForeignKey(Student,null=True)
	fee_category = models.ForeignKey(FeeCategory)
	fee_paid = models.DecimalField(max_digits=6, decimal_places=2,default=0)
	date_of_payment = models.DateField(auto_now_add=True,blank=True)
	month = models.CharField(max_length=9, choices=MONTH_CHOICES, default='1')
	class Meta:
		unique_together = (('student', 'month'),)



	
