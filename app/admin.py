from django.contrib import admin

# Register your models here.
from .models import Fib

admin.site.register(Fib)
