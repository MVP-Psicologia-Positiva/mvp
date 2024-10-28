from rest_framework import serializers
from .models import historicalSessions

class historicalSessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = historicalSessions
        fields = ('id','username','sessionDate')
