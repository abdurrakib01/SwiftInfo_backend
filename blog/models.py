from django.db import models
from django.conf import settings
# Create your models here.

class Blog (models.Model):
    image = models.ImageField(upload_to="Blog_Image/", default="assets/topic3.png")
    title = models.CharField(max_length=100)
    info = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title