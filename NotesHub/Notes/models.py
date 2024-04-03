from django.db import models
import json


class UserData(models.Model):
    user_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=100, null=False)
    all_notes = models.JSONField(default=dict)
    favourite_notes = models.JSONField(default=dict)

    def __str__(self):
        return self.email
