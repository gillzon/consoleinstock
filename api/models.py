from django.db import models

# Create your models here.
import uuid

# Create your models here.


class StockStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message = models.CharField(max_length=300)
    vendor = models.CharField(max_length=300)
    instock = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
