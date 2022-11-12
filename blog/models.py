from django.db import models

# Create your models here.

class Blog (models.Model):
    image = models.ImageField(upload_to="Blog_Image", blank=True)
    title = models.CharField(max_length=100)
    info = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title