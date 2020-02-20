from rest_framework import serializers
from . import models

class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dictionary
        fields = '__all__'