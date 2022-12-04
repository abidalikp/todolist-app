from django.db import models
from django.contrib.auth.models import User

class Todolist(models.Model):
    text = models.CharField(max_length=45)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.text