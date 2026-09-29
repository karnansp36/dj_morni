from django.db import models
from user_auth.models import Users_data
# Create your models here.

class SocialPost(models.Model):
    user = models.ForeignKey(Users_data, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='social_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title