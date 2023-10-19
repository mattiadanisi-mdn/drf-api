from typing import Any
from django.db import models
from django.contrib.auth.models import User as BaseUser
import uuid
    

class User(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    def __str__(self) -> str:
        return f'{self.user.username}'
    
    def delete(self, *args, **kwargs):
        BaseUser.objects.get(id=self.user.id).delete()
        return super().delete(*args, **kwargs)
        




    
