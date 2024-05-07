from django.db import models

class Contact(models.Model):
    class Role(models.TextChoices):
        ADMIN = 'Admin', 'Admin'
        USER = 'User', 'User'
        GUEST = 'Guest', 'Guest'

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.USER)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    creation_data = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} | {self.role}"
