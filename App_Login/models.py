from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


# Create your models here.
class CreateUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('You have must Email')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create_renter(self, email, password):
        user = self.create_user(email, password)
        user.is_renter = True
        user.save(using=self._db)
        return user

    def create_renter(self, email, password):
        user = self.create_user(email, password)
        user.is_owner = True
        user.save(using=self._db)
        return user


class CreateUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=100)
    is_renter = models.BooleanField('is_renter', default=False)
    is_staff = models.BooleanField('is_staff', default=False)
    is_owner = models.BooleanField('is_owner', default=False)
    is_active = models.BooleanField(default=True)


    objects = CreateUserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class user_registration(models.Model):
    user = models.OneToOneField(CreateUser, related_name='user_profile', on_delete=models.CASCADE)
    Full_name = models.CharField(max_length=400, blank=True, null=True)
    User_email = models.EmailField(blank=True, null=True)
    User_phone = models.IntegerField(blank=True, null=True)
    NID_photo = models.ImageField(blank=True, null=True, upload_to='user_nid')
    User_image = models.ImageField(blank=True, null=True, upload_to='user_pics')
    Address = models.TextField(blank=True, null=True)
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Full_name + self.User_email

