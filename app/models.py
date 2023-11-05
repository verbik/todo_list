from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Task(models.Model):
    content = models.CharField(max_length=255)
    creation_datetime = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True)
    is_done = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tags")
