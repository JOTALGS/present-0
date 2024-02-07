from django.db import models
import uuid
from accounts.models import User
from django.utils.timesince import timesince

# Create your models here.

class PostAttachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='post_attachments')

    owner = models.ForeignKey(User, related_name='posts_attachments', on_delete=models.CASCADE)



class Posts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(blank=True, null=True)
    attachments = models.ManyToManyField(PostAttachment, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)

    def created_since(self):
        return timesince(self.created_at)