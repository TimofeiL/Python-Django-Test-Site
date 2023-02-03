from django.db import models

class worker(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    second_name = models.CharField(max_length=40, blank=False)
    age = models.CharField(default=18, max_length=3)

    def __str__(self):
        return f'{self.second_name} {self.first_name}'