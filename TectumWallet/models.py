from django.db import models
from django.contrib.auth.models import User
from datetime import datetime   
# Create your models here.
class Wallet(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     balance = models.FloatField()
     def __str__(self):
         return self.user.username
class Transaction(models.Model):
    user_from = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_to")
    user_to = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_from')
    amount = models.FloatField()
    date_time= models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.user_from.username
