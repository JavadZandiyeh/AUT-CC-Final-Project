# from django.db import models

# # Create your models here.
# class Coin(models.Model):
#    coin_name = models.CharField(max_length=30)
#    timestamp = models.DateTimeField(auto_now_add=True)
#    price = models.FloatField()

#    def __str__(self):
#       return f"{self.coin_name}, {self.timestamp}, {self.price}"

# class CoinAlertSubscription(models.Model):
#    email = models.EmailField(max_length=200)
#    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
#    difference_percentage = models.IntegerField()

#    def __str__(self):
#       return f"{self.email}, {self.coin_name}, {self.difference_percentage}"