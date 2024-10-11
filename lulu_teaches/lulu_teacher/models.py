from django.db import models

class historicalSessions(models.Model):
    sessionDate = models.DateTimeField("session date")
    username = models.CharField(max_length=255)