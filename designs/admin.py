from django.contrib import admin

# Register your models here.
from .models import Design, Comment, Tag

admin.site.register(Design)
admin.site.register(Comment)
admin.site.register(Tag)
