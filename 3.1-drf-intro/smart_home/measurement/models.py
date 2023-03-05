from django.db import models
from django.utils import timezone

class transmitter(models.Model):
    # id = models.IntegerField(primary_key=True)
    # id = models.ForeignKey('temperature_measure', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

class temperature_measure(models.Model):
    # id = models.IntegerField()
    ids = models.ForeignKey('transmitter', on_delete=models.CASCADE, related_name= 'ids')
    value = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add = False)

    # def publish(self):
    #     self.date = timezone.now()
    #     self.save()