from django.db import models


class Contactus(models.Model):
    name = models.CharField(max_length=50, )
    phone = models.CharField(max_length=12, unique=True)
    email = models.EmailField(blank=True, null=True)
    text = models.TextField()

    def __str__(self):
        return self.name
