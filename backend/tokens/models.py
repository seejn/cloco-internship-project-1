from django.db import models
from django.core.validators import MaxValueValidator

from users.models import CustomUser

import math, time

# Create your models here.
class Token(models.Model):

    expiry_time = math.floor(time.time()) + 84600

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="token")
    t_type = models.CharField(max_length=50, null=True, unique=True)
    token = models.CharField(max_length=250, unique=True)
    expiry = models.PositiveIntegerField(default=expiry_time, validators=[MaxValueValidator(99999999999)])

    class Meta:
        db_table = 'tokens'

    def is_token_expired(self):
        curr_time = math.floor(time.time())
        print("curr-time", curr_time)
        print("expiry_time", self.expiry)
        if curr_time > self.expiry:
            self.delete()
            return True

        return False

    def __str__(self):
        return self.t_type