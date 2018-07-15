from django.db import models
from datetime import datetime
# Create your models here.

class Outcome(models.Model):
    value = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.CharField(max_length=64)
    subcategory = models.CharField(max_length=64)
    account = models.CharField(max_length=64)
    happend_at = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.category + "/" + self.subcategory + "(-" + str(self.value) + ")" 