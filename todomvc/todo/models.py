from django.db import models

class Todos(models.Model):
    title = models.CharField(max_length=45)
    completed = models.BooleanField(default=False)
    order = models.IntegerField(null=True)
