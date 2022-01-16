from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Account(models.Model):
    """That is bank account table. To save users data."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    iban = models.CharField(max_length=22, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"