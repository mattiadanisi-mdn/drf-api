from django.db import models
import uuid
from django.conf import settings

from animal.models import Animal
from user.models import User

class Adoption(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.animal.race} | {self.owner.username}'
