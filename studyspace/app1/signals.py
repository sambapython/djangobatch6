from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from app1.models import UserProfile1

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	
	up = UserProfile1(user=instance, up_name=instance.username+"_profile")
	up.save()
    # up = UserProfile(user_ptr=instance, up_name=instance.username+"_profile")
    # up.save()