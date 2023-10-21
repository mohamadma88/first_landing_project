from django.db import models


class Boxproject(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()


    def __str__(self):
        return self.title
