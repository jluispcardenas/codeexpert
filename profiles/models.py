from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):  
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    current_runtime = models.CharField(max_length=250, default='')  
    bio = models.TextField(null=True)
    accepted = models.IntegerField(null=True, default=0)
    submissions = models.IntegerField(null=True, default=0)

    def __str__(self):
        return 'Profile: {}'.format(self.user.username)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)