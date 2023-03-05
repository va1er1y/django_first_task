from django.db import models
# from django_extensions import AutoSlugField
from django_extensions.db.fields import AutoSlugField

class Phone(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from="name", max_length=150, default="items")
    price = models.FloatField(max_length=10)
    image = models.CharField(max_length=500)
    release_date = models.CharField(max_length=20)
    lte_exists = models.BooleanField()



