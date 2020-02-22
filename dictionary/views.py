from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

from rest_framework import generics

# Create your views here.

class Dictionary_View(viewsets.ReadOnlyModelViewSet):
    queryset =models.Dictionary.objects.all()
    serializer_class =serializers.DictionarySerializer

class Dictionary1_View(viewsets.ModelViewSet):
    queryset = models.Dictionary.objects.filter(alpha='ㄱ')
    serializer_class = serializers.DictionarySerializer

class Dictionary2_View(viewsets.ModelViewSet):
    queryset = models.Dictionary.objects.filter(alpha='ㄴ')
    serializer_class = serializers.DictionarySerializer

class Dictionary3_View(viewsets.ModelViewSet):
    queryset = models.Dictionary.objects.filter(alpha='ㄷ')
    serializer_class = serializers.DictionarySerializer

class Dictionary4_View(viewsets.ModelViewSet):
    queryset = models.Dictionary.objects.filter(alpha='ㄹ')
    serializer_class = serializers.DictionarySerializer

class Dictionary5_View(viewsets.ModelViewSet):
    queryset = models.Dictionary.objects.filter(alpha='ㅁ')
    serializer_class = serializers.DictionarySerializer

class Dictionary6_View(viewsets.ModelViewSet):
    queryset = models.Dictionary.objects.filter(alpha='ㅂ')
    serializer_class = serializers.DictionarySerializer

class Dictionary7_View(viewsets.ModelViewSet):
    queryset = models.Dictionary.objects.filter(alpha='ㅅ')
    serializer_class = serializers.DictionarySerializer

class Dictionary8_View(viewsets.ModelViewSet):
    queryset = models.Dictionary.objects.filter(alpha='ㅇ')
    serializer_class = serializers.DictionarySerializer

class Dictionary9_View(viewsets.ModelViewSet):
    queryset = models.Dictionary.objects.filter(alpha='ㅈ')
    serializer_class = serializers.DictionarySerializer

class Dictionary10_View(viewsets.ModelViewSet):
    queryset = models.Dictionary.objects.filter(alpha='ㅊ')
    serializer_class = serializers.DictionarySerializer

class Dictionary11_View(viewsets.ModelViewSet):
    queryset = models.Dictionary.objects.filter(alpha='ㅋ')
    serializer_class = serializers.DictionarySerializer

class Dictionary12_View(viewsets.ModelViewSet):
    queryset = models.Dictionary.objects.filter(alpha='ㅌ')
    serializer_class = serializers.DictionarySerializer

class Dictionary13_View(viewsets.ModelViewSet):
    queryset = models.Dictionary.objects.filter(alpha='ㅍ')
    serializer_class = serializers.DictionarySerializer

class Dictionary14_View(viewsets.ModelViewSet):
    queryset = models.Dictionary.objects.filter(alpha='ㅎ')
    serializer_class = serializers.DictionarySerializer