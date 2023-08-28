from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=69)

    # @property
    # def full_name(self):
    #     """_summary_

    #     Returns:
    #         _type_: _description_
    #     """
    #     return f'{self.user.first_name} {self.user.last_name}'