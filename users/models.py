from django.db import models
from django.urls import reverse

# Create your models here.
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin




class MyUserManager(BaseUserManager):
    def create_user(self, username,email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.is_staff=False
        user.save(using=self._db)
        return user

    def create_superuser(self,username, email, date_of_birth, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            date_of_birth=date_of_birth ,


        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username=models.CharField(max_length=60,unique=True)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    poweruser =  models.BooleanField(default=False)
    creator =  models.BooleanField(default=False)
    profile_image = models.ImageField(max_length=255,upload_to='static/images',default='static/images/default.jpg')
    last_login = models.DateTimeField(verbose_name='last login',auto_now=True)
    date_joined = models.DateTimeField(verbose_name='date joined',auto_now_add=True)


    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def get_absolute_url(self):
        return reverse('users:profile_view',args=[self.username,self.date_of_birth.year,self.date_of_birth.month,self.date_of_birth.day])

