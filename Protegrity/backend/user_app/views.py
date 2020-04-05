from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import User_AppSerializer      # add this
from user_app.models import User_App                     # add this

class User_AppView(viewsets.ModelViewSet):
    serializer_class = User_AppSerializer
    queryset = User_App.objects.all()
