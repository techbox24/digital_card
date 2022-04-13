from django.db import models

class User(models.Model):    
    id = models.BigIntegerField(primary_key=True)
    discord_id = models.CharField(max_length=120)
    avatar = models.CharField(max_length=100)
    email = models.EmailField()
    wordle = models.IntegerField(default=0)
    papertoss = models.IntegerField(default=0)
    total_score = models.IntegerField(default=0)