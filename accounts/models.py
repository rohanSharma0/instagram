from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

# Create your models here.
class Profile(models.Model):

        user = models.OneToOneField(User, on_delete=models.CASCADE)
        display_name = models.CharField(max_length=40,blank=True)
        profile_image = models.ImageField(default='defaultprofilepic.jpg',upload_to='profileImg')

        def __str__(self):
                return f'{self.user.username} Profile'

        def save(self, **kwargs):
                super().save()

                img = Image.open(self.profile_image.path)
                if img.height > 300 or img.width > 300:
                        output_size = (300,300)
                        img.thumbnail(output_size)
                        img.save(self.profile_image.path)

@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created,**kwargs):
        if created:
                Profile.objects.create(user=instance)  

@receiver(post_save, sender=User)
def save_user_profile(sender,instance,**kwargs):
        instance.profile.save()
