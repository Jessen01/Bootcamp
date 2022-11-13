from django.db import models

from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #one to one field
    birth_date = models.DateField()
    has_pet = models.BooleanField(default=True)
    number_pet = models.IntegerField()

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def person_age(self):
        current_date = date.today()
        current_age = current_date.year-self.birth_date.year
        return f'{current_age}'
