import random
import string

from django.db import models
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import BaseUserManager, AbstractUser, \
    PermissionsMixin


# Create your models here.
class MainUserManager(BaseUserManager):
    """
    Main user manager
    """

    def create_user(self, username, password=None, is_active=None, **kwargs):
        """
        Creates and saves a user with the given username and password
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        if is_active is not None:
            user.is_active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password
        """
        user = self.create_user(username, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.is_moderator = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class MainUser(AbstractUser):
    username = models.CharField(max_length=100, blank=False, unique=True,
                                db_index=True, verbose_name='Username')
    first_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Фамилия')
    email = models.EmailField(blank=True, null=True, verbose_name='Почта')
    password = models.CharField(blank=True, null=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = MainUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    @property
    def is_authenticated(self):
        return True

    def full(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
        }


class ConfirmationCode(models.Model):
    code = models.CharField(unique=True, max_length=200)
    user = models.ForeignKey(MainUser, related_name='codes', on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.get_code()
        super(ConfirmationCode, self).save(*args, **kwargs)

    def get_code(self):
        current_codes = list(ConfirmationCode.objects.values_list('code', flat=True))
        while True:
            code = self.generate_code()
            if code not in current_codes:
                break
            else:
                continue
        return code

    @staticmethod
    def generate_code():
        chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choice(chars) for x in range(6,12))
