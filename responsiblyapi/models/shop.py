from django.db import models
# from django.contrib.auth.models import User

class Shop(models.Model):
    """we be shopping"""

    title = models.CharField(max_length=70)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.URLField()
    asap = models.BooleanField()
    # client = models.ForeignKey("Client", on_delete=models.CASCADE)
    # client = models.ManyToOneField(Client, on_delete=models.CASCADE)
