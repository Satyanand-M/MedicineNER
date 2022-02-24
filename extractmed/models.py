from django.db import models

# Create your models here.
class Medicine(models.Model):
    Medicine_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    Medname = models.CharField(max_length=50)
    Manufacturer = models.CharField(max_length=100)