from django.db import models
from django.conf import settings
# Create your models here.

class Blog (models.Model):
    image = models.ImageField(upload_to="Blog_Image", blank=True, null=True)
    title = models.CharField(max_length=100)
    info = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title