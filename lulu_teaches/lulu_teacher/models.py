from django.db import models
from django.contrib.auth.models import User

class historicalSessions(models.Model):
    sessionDate = models.DateTimeField("session date")
    username = models.ForeignKey(User, on_delete=models.CASCADE)

class luluTrainning(models.Model):
    version_title = models.CharField(max_length=255)
    attachments = models.FileField(upload_to='uploads/%Y/%m/%d/')
    comments = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)

class UsersMilestones(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    milestone = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)