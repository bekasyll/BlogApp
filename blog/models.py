from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField(blank=False)
    date_posted = models.DateTimeField(default=timezone.now, blank=False)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

    class Meta:
        verbose_name = "Posts"
        verbose_name_plural = "Posts"
        db_table = "posts"
        ordering = ["title"]
        indexes = [models.Index(fields=["title"])]

    def __str__(self):
        return self.title