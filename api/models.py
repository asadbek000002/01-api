from django.db import models


class Talaba(models.Model):
    ism = models.CharField(max_length=30)
    familya = models.CharField(max_length=30)
    yosh = models.CharField(max_length=10)
    image = models.ImageField()
    number = models.CharField(max_length=13)

    def __str__(self):
        return f'{self.ism} | { self.familya}'