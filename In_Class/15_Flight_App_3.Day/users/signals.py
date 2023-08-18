#!0708 (post_save, sender=User)  userda save isleminden sonra calis(create_token calis) demek bu parametreler.


from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import  Token

@receiver(post_save, sender=User)
def create_token(sender, instance, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



#!burayi olusturduktan sonra apps.py git. yazdigin signali import et. 