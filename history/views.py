from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here.

class History_View(viewsets.ModelViewSet):
    queryset = models.History.objects.all()
    serializer_class = serializers.HistorySerializer