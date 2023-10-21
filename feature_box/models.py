from django.db import models


class Feature(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=150)

    def __str__(self):
        return self.title
