from django.db import models
from django.contrib.auth.models import User

# class user(models.Model) :
#     name=models.CharField(max_length=100)
#     email=models.CharField(max_length=100)
#     password=models.CharField(max_length=20)



class AudioFile(models.Model):
    podcastname = models.CharField(max_length=200)
    podcast_des = models.TextField(max_length=200)
    podcast_speaker = models.TextField(max_length=200)
    podcast_id= models.AutoField(primary_key=True)
    file = models.FileField(upload_to='audio_pod/')
    file1 = models.FileField(upload_to='uploads/')
    file2= models.FileField(upload_to='video_pod')

    def __str__(self) :
        return str(self.podcast_id)
        

class UserLikedAudio(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio = models.CharField(max_length=10000000, default="")