from django.db import models


class Testimonial(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=150)

    def __str__(self):
        return self.title
