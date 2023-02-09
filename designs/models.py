from django.db import models
import uuid
# Create your models here.


class Design(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    design_link = models.CharField(max_length=2500, null=True, blank=True)
    tags = models.ManyToManyField('Tags', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    RATING_TYPE = (
        ('like', 'Liked'),
        ('dislike', 'Disliked')
    )
    #user = 
    design = models.ForeignKey(Design, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    rating = models.CharField(max_length=250, choices=RATING_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value


class Tags(models.Model):
    name = models.Charfield(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name