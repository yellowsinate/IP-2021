from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from . import models
from . import serializers

class FacultyViewset(viewsets.ModelViewSet):
    queryset = models.Faculty.objects.all()
    serializer_class = serializers.FacultySerializer
    
class UserViewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer