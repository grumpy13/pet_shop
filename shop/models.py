from django.db import models


class Pet(models.Model):
	SEX_CHOICES = (
	("MALE", "Male"),
	("FEMALE", "Female"),
	)

	name = models.CharField(max_length=120)
	age = models.IntegerField()
	sex = models.CharField(max_length=120, choices=SEX_CHOICES, default="FEMALE")
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return self.name