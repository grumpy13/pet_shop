from django.db import models

class Pet(models.Model):
	FEMALE = "Female"
	MALE = "Male"
	SEX = [
		(FEMALE, FEMALE),
		(MALE, MALE)
	]
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	sex = models.CharField(max_length=10, choices=SEX)
	price = models.DecimalField(max_digits=10, decimal_places=3)

	def __str__(self):
		return self.name
