from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class CustomUser(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(_("email address"),unique=True)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    date_join=models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects=CustomUserManager()

    def __str__(self):
        return f"{self.email}"
    

class UserProfile(models.Model):
    """
        detail of user information
    """
    user_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='profile')
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    mobile=models.IntegerField(null=True)
    national_code=models.CharField(max_length=10)
    image=models.ImageField(upload_to='image/user')

    def __str__(self):
        return f"{self.user_id} {self.first_name}"





@receiver(post_save, sender=CustomUser)
def register_profile(sender, instance, created, **kwargs):
    """
    register created user_id in profile when user created
    """
    UserProfile.objects.get_or_create(user_id=instance)
    Token.objects.get_or_create(user=instance)

