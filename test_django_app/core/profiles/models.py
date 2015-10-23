from django.db import models #import the models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Profile(AbstractUser):
	AnimalChoices = (
		('dog', 'dog'),
		('cat', 'cat'),
		('fish', 'fish'),
		('panda', 'panda'),
	)
	user_type = (
		(0, 'user_type_1'),
		(1, 'user_type_2'),
		(2, 'user_type_3'),
	)
	favorite_animal = models.CharField(max_length=250, choices=AnimalChoices, null=True, blank=True)


