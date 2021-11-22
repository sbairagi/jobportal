from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CreateJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_name = models.CharField(max_length=50)
    job_desc= models.TextField()
    experience = models.IntegerField()
    open_position = models.IntegerField()
    


class ApplyUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.CharField(max_length=50)
    resume = models.FileField(upload_to ='uploads/')