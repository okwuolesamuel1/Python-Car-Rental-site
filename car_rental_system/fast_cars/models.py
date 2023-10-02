from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=50, default='Black')
    rent_price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image_link = models.URLField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"Booking #{self.pk} - User: {self.user.username} - Car: {self.car.name}"
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    

class Review(models.Model):
    title = models.CharField(max_length=100)
    content =  models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('testimonial-detail',  kwargs={'pk': self.pk})
