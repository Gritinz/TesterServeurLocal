from django.db import models

# Create your models here.

class Counter(models.Model):
    value = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Counter: {self.value}"