from django.db import models


class calc(models.Model):
    count1 = models.IntegerField(default=0)
    count2 = models.IntegerField(default=0)
    app = models.CharField(max_length=2)
