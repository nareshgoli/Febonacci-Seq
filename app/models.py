# from __future__ import unicode_literals
from django.db import models

class Fib(models.Model):
    number = models.IntegerField()
    result = models.IntegerField()
    time_taken = models.CharField(max_length=255)

    # class Meta:
    #     db_table = 'fibonacci_results'
    

    def __str__(self):
        return self.number
