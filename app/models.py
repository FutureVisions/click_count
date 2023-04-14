from django.db import models

class Button(models.Model):
    click_count = models.IntegerField(default=0)

# Create your models here.
