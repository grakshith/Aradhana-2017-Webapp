from __future__ import unicode_literals
import uuid
from django.db import models

# Create your models here.
class Event(models.Model):
	CHOICES = (
		('Class 1-4',"Class 1 to 4"),
		('Class 5-7',"Class 5 to 7"),
		('Class 8-10',"Class 8 to 10"),
		)
	name = models.CharField(max_length=100)
	category = models.CharField(max_length=100,
		choices=CHOICES,
		default="Select")
	TYPE_CHOICES = (
		("Individual Event","Individual Event"),
		("Team Event","Team Event"),
		)
	type= models.CharField(max_length=100,
		choices=TYPE_CHOICES,
		default="Select")
	first_place = models.TextField(default="TBD")
	second_place = models.TextField(default="TBD")
	third_place = models.TextField(default="TBD")
	def __str__(self):
		return ''.join(self.name+" - "+self.category)

class Student(models.Model):
	#id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=100)
	standard = models.IntegerField()
	school = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	events = models.ManyToManyField(Event)
	def __str__(self):
		return ''.join(self.name+" - "+self.school)

