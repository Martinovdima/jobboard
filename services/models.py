from django.db import models


class ServicesCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Transcrib(models.Model):
    name = models.CharField(max_length=256, unique=True)
    audio = models.FileField(upload_to='audio', blank=True)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} '
