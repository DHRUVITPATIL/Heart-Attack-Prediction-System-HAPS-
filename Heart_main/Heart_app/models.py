from django.db import models
from django.contrib.auth.models import User

class PredictionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    features = models.TextField()  # Or use JSONField for structured data if using Django 3.1+
    prediction = models.CharField(max_length=30)

    def __str__(self):
        return f"Prediction for {self.user.username} on {self.date.strftime('%Y-%m-%d %H:%M')}"
