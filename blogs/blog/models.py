from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=255)
    post_text = models.TextField()
    post_likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.author}"

    def get_absolute_url(self):
        return reverse('check_post', args=(self.pk, ))
