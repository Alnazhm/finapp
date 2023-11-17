from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Account(AbstractUser):
      CURATOR = 1
      REVIEWER = 2
      
      ROLE_CHOICES = (
          (CURATOR, 'Curator'),
          (REVIEWER, 'Reviewer'),
      )
      role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=1)


