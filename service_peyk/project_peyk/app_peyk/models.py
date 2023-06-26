from django.db import models

class Coin(models.Model):
    coin_name = models.CharField(max_length=100, primary_key=True)

    class Meta:
        db_table = "Coin"

class Prices(models.Model):
    coin_name = models.CharField(max_length=100)
    time_stamp = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(null=False)
   
    class Meta:
        unique_together = (("coin_name", "time_stamp"),)
        db_table = "Prices"
    
class AlertSubscriptions(models.Model):
    email = models.CharField(max_length=100)
    coin_name = models.CharField(max_length=100)
    difference_percentage = models.IntegerField(null=False)

    class Meta:
        unique_together = (("email", "coin_name"),)
        db_table = "AlertSubscriptions"
    
    def __str__(self) -> str:
        return {
            "email": self.email,
            "coin_name": self.coin_name,
            "percentage": self.difference_percentage
        }