from django.db import models


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
            return self.name


class InventoryItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    locations = models.ForeignKey('Location', on_delete=models.CASCADE, null= True, blank=True) #Made temporarily nullable
    barcode = models.CharField(max_length=225, blank=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
