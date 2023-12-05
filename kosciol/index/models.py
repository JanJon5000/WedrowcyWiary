from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField(max_length=10000)
    googleMap = models.TextField(max_length=1000, default='')

    published = models.DateField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published']
        indexes = [
            models.Index(fields=ordering)
        ]

    def __str__(self):
        return self.title
    
    def publish(self):
        self.save()