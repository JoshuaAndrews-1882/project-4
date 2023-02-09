from django.db import models
import uuid
# Create your models here.


class Design(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    design_link = models.CharField(max_length=2500, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
