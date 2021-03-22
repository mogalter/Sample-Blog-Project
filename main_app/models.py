from django.db import models
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
# users, posts


class Post(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # auto_now=True would set date posted to current time everytime we update
    # auto_now_add=True would set date posted to current time everytime we create it
    # however, we'll never be able to update it
    # default = timezone.now passes in the function for later execution
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # One author can make many posts, but each post has an author
    # One to many relationship

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

