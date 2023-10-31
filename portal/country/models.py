from django.db import models

# Create your models here.
class country(models.Model):
    country_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=20)

    def __str__(self):
        return self.country_name