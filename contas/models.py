# contas/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_groups',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_permissions',
        blank=True,
        help_text='Specific permissions for this user.'
    )

    def __str__(self):
        return self.username