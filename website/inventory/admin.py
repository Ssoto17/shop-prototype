from django.contrib import admin
from .models import InventoryItem, Location


admin.site.register(InventoryItem)
admin.site.register(Location)