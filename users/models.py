from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser


class CustomUser(AbstractUser):
    ROLE = (
        ("SUPER_ADMIN", "SUPER_ADMIN"),
        ("ADMIN", "ADMIN"),
    )
    role = models.CharField(max_length=20, choices=ROLE, default="ADMIN")

    def __str__(self) -> str:
        return self.get_full_name() or self.username
