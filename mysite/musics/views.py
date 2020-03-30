from django.shortcuts import render
from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer
from django.http import JsonResponse
from django.http import HttpResponse


from rest_framework import viewsets


# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset= Profile.objects.all()
    serializer_class = ProfileSerializer
    
