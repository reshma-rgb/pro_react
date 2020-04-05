from django.db import models

# Create your models here.
class User_App(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField( max_length=50)
    user_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    role_name = models.CharField(max_length=50)
    roles = models.CharField(max_length=240)
    role_discription = models.CharField(max_length=100)


    def __str__(self):
        return self.user_name
