from django.db import models
from users.models import CustomUser
from services.models import Service

class Order(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')],
        default='Pending'
    )
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.username} - {self.service.name} ({self.status})"