from django.db import models


# Create your models here.
class Coin(models.Model):
    side = models.CharField(choices=(('o', 'o'), ('r','r')), max_length=5)
    game_time = models.DateTimeField(auto_now_add=True)
