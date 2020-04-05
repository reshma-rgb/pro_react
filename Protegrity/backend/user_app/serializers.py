from rest_framework import serializers
from user_app.models import User_App

class User_AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_App
        fields = ('id','user_name','role_name','first_name','last_name','description','roles','role_discription')
