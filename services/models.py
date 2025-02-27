from django.db import models
from users.models import CustomUser

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    average_rating = models.FloatField(default=0.0)

    def update_average_rating(self):
        reviews = self.reviews.all()
        if reviews:
            self.average_rating = sum(review.rating for review in reviews) / len(reviews)
        else:
            self.average_rating = 0.0
        self.save()

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.service.update_average_rating()

    def __str__(self):
        return f"{self.user.username} - {self.service.name} ({self.rating})"