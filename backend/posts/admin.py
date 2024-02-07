from django.contrib import admin
from .models import PostAttachment, Posts


# Register your models here.

admin.site.register(Posts)
admin.site.register(PostAttachment)