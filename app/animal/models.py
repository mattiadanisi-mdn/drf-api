from django.db import models
import uuid
from datetime import date

class Animal(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    race = models.CharField(max_length=256, blank=False, null=False)
    birthday = models.DateField(blank=False, null=False)

    @property
    def age(self):
        animal_age = date.today() - self.birthday
        return int((animal_age).days/365.25)

    def __str__(self):
        return f'{self.race}____{self.uuid}'
    
        

    
