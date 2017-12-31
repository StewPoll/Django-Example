from django.db import models
import uuid


class Post(models.Model):
    """
    Creating a post class here, not that we use it but mainly so we have something to create migrations for.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    title = models.CharField(max_length=150)
    content = models.TextField()

    def status(self):
        return 'Published' if self.published else 'Draft'

    def __str__(self):
        return f'{self.title} - ({self.status()})'
