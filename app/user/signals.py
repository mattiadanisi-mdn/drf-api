from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User as BaseUser
from user.models import User

@receiver(post_save, sender=BaseUser)
def base_user_post_save_receiver(sender, created, instance, **kwargs):
    if created:
        User.objects.create(user=instance)
