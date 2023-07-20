from django.db import models
# from django.contrib.auth.models import User

class Shop(models.Model):
    """we be shopping"""

    title = models.CharField(max_length=70)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    asap = models.BooleanField()
    # client = models.ForeignKey("Client", on_delete=models.CASCADE, related_name='client')
    # client = models.ManyToManyField("Client", on_delete=models.CASCADE, related_name='clients')
    client = models.ManyToManyField("Client", related_name='shops')
    