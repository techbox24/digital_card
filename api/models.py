from django.db import models
# from django.contrib.auth.models import UserManager

# Create your models here.
# class CustomUserManager(UserManager):
#     def create_new_user(self, user):
#         new_user = self.create_user(
#             id = user['id'],
#             discord_id = f"{user['username']}#{user['discriminator']}",
#             avatar = user['avatar'],
#             email = user['email'],
#             name = "",
#             wordle = 0,
#             papertoss = 0,
#             points_spent = 0
#         )
#         return new_user

class User(models.Model):    
    id = models.BigIntegerField(primary_key=True)
    discord_id = models.CharField(max_length=120)
    avatar = models.CharField(max_length=100)
    email = models.EmailField()
    name = models.CharField(max_length=100, default="")
    wordle = models.IntegerField(default=0)
    papertoss = models.IntegerField(default=0)
    points_spent = models.IntegerField(default=0)
    last_login = models.DateTimeField(null=True)
