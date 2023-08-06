from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    def create_user(self, email, **extra_fields):
        """
        Methode creates user
        :param email: str
        :param extra_fields: dict
        :return: User
        """
        if not email:
            raise ValueError("User must have email number")

        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password()
        user.save()
        return user

    def create_superuser(self, email, password):
        """
        Methode creates superuser
        :param email: str
        :param password: str
        :return: superuser
        """
        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.user_type = 'admin'
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User model"""

    user_type_choices = [
        ('client', 'Клиент'),
        ('expert', 'Эксперт'),
        ('admin', 'Администратор')
    ]
    specialization_choices = [
        ('ugolovnyi', 'Уголовный кодекс'),
        ('semeinyi', 'Семейный кодекс'),
        ('nalogovyi', 'Налоговый кодекс'),
        ('grajdanskyi', 'Гражданский кодекс'),
        ('trudovoyi', 'Трудовой кодекс'),
        ('budjetnyi', 'Бюджетный кодекс')
    ]

    username = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=255, choices=user_type_choices)
    specialization = models.CharField(max_length=255, choices=specialization_choices, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    contact = models.CharField(max_length=255, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return f'{self.email}'
