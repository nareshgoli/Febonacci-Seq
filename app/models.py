from django.db import models

class Fib(models.Model):
    number = models.IntegerField()
    result = models.FloatField()
    time_taken = models.CharField(max_length=255)    

    def __str__(self):
        return self.number
