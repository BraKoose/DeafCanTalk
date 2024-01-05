from django.db import models

# Create your models here.

class Languages(models.Model):
    name= models.CharField(max_length=100)
    

    
    
class Booking(models.Model):
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('completed', 'Complete')])
    
    def __str__(self):
        return f'{self.client_name} - {self.start_time}'
    
class VideoContent(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    youtube_link = models.URLField(blank=True)
    video_description = models.TextField()
    
    def __str__(self):
        return f'{self.title} - {self.video_description}'