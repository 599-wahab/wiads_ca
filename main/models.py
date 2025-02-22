from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """A user profile model that extends the built-in User model."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    def __str__(self):
        return self.user.username
