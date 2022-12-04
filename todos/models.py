import uuid

from django.db import models

from users.models import User


class Todo(models.Model):
    class Status(models.TextChoices):
        TODO = 'TODO', 'TODO'
        DONE = 'DONE', 'DONE'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=20)
    detail = models.TextField()
    status = models.CharField(max_length=10, choices=Status.choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
